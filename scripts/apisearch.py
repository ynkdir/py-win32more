# /// script
# dependencies = ["win32more"]
# ///

import argparse
import io
import json
import logging
import urllib.request
import zipfile
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from win32more.Microsoft.UI.Xaml import FocusState
from win32more.winui3 import XamlApplication, XamlLoader

APILIST_CACHE = Path(".apisearch.txt")
LIST_MAX = 200
METADATA_URLS = [
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Windows.SDK.Win32Metadata.68.0.4-preview.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Windows.SDK.Contracts.10.0.26100.7175.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.WindowsAppSDK.1.8.251106002.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Web.WebView2.1.0.3595.46.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.1.0/Microsoft.Graphics.Win2D.1.3.2.zip",
]

logger = logging.getLogger(__name__)


class App(XamlApplication):
    def __init__(self):
        super().__init__()

        if APILIST_CACHE.exists():
            self._apilist = json.loads(APILIST_CACHE.read_text())
        else:
            self._apilist = ApiListGenerator().generate()
            logger.info(f"writing cache file {APILIST_CACHE}")
            APILIST_CACHE.write_text(json.dumps(self._apilist))

    def OnLaunched(self, args):
        self.Window = XamlLoader.Load(
            self,
            """
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*"/>
        </Grid.ColumnDefinitions>
        <TextBox x:Name="TextBlock1" Grid.Row="0" PlaceholderText="Enter API name" TextChanged="TextBlock1_TextChanged" Loaded="TextBlock1_Loaded"/>
        <ListView x:Name="ListView1" Grid.Row="1" />
    </Grid>
</Window>
""",
        )

        self.Window.Title = "Api Search"
        self.Window.Activate()

    def TextBlock1_TextChanged(self, sender, e):
        query = self.TextBlock1.Text.lower()
        items = self.ListView1.Items
        items.Clear()

        if query == "":
            return

        count = 0
        for api in self._apilist:
            if query in api["FQN"].lower():
                items.Append(
                    XamlLoader.Load(
                        self,
                        f'<TextBlock xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation">{self.format_api(api)}</TextBlock>',
                    )
                )
                count += 1
                if count == LIST_MAX:
                    items.Append(f"... (over {LIST_MAX})")
                    break

    def TextBlock1_Loaded(self, sender, e):
        self.TextBlock1.Focus(FocusState.Programmatic)

    def format_api(self, api: Any) -> str:
        link = self.format_doc(api)
        if "Method" in api:
            return f"{api['Namespace']}.<Run Foreground='Tomato'>{api['Class']}</Run>.<Run Foreground='Maroon'>{api['Method']}</Run> {link}"
        elif "Field" in api:
            return f"{api['Namespace']}.<Run Foreground='Tomato'>{api['Class']}</Run>.<Run Foreground='Maroon'>{api['Field']}</Run> {link}"
        return f"{api['Namespace']}.<Run Foreground='Tomato'>{api['Name']}</Run> {link}"

    def format_doc(self, api: Any) -> str:
        if api["Doc"] is None:
            return ""
        return f"""<Hyperlink NavigateUri="{api["Doc"]}">doc</Hyperlink>"""


class MetadataLoader:
    def download(self, url: str) -> bytes:
        logger.info(f"download: {url}")
        with urllib.request.urlopen(url) as f:
            return f.read()

    def download_zip(self, url: str) -> zipfile.ZipFile:
        data = self.download(url)
        file = io.BytesIO(data)
        return zipfile.ZipFile(file)

    def load_files(self, metadata_files: list[zipfile.ZipPath]) -> Any:
        js = []
        for zfile in metadata_files:
            for zname in zfile.namelist():
                zpath = zipfile.Path(zfile, zname)
                js.extend(json.loads(zpath.read_text()))
        return js

    def load(self):
        meta = self.load_files([self.download_zip(url) for url in METADATA_URLS])
        return list(self.preprocess(meta))

    def preprocess(self, meta: Any) -> Iterable[Any]:
        for td in meta:
            if "WindowsRuntime" in td["Attributes"]:
                if td["Namespace"] == "" or td["BaseType"] == "System.Attribute":
                    continue
            else:
                if td["Namespace"] == "" or "Public" not in td["Attributes"]:
                    continue
            yield td

        return meta


class ApiListGenerator:
    def generate(self):
        meta = MetadataLoader().load()
        logger.info("generating api list")
        return list(self.enumerate_name(meta))

    def enumerate_name(self, meta: Any) -> Iterable[str]:
        for td in meta:
            if td["Name"] == "Apis":
                for fd in td["Fields"]:
                    yield {
                        "Namespace": td["Namespace"],
                        "Name": fd["Name"],
                        "FQN": f"{td['Namespace']}.{fd['Name']}",
                        "Doc": self.get_doc(fd["CustomAttributes"]),
                    }
                for md in td["Methods"]:
                    yield {
                        "Namespace": td["Namespace"],
                        "Name": md["Name"],
                        "FQN": f"{td['Namespace']}.{md['Name']}",
                        "Doc": self.get_doc(md["CustomAttributes"]),
                    }
            else:
                yield {
                    "Namespace": td["Namespace"],
                    "Name": td["Name"],
                    "FQN": f"{td['Namespace']}.{td['Name']}",
                    "Doc": self.get_doc(td["CustomAttributes"]),
                }
                for fd in td["Fields"][1:]:
                    yield {
                        "Namespace": td["Namespace"],
                        "Class": td["Name"],
                        "Field": fd["Name"],
                        "FQN": f"{td['Namespace']}.{td['Name']}.{fd['Name']}",
                        "Doc": self.get_doc(fd["CustomAttributes"]),
                    }
                for md in td["Methods"]:
                    yield {
                        "Namespace": td["Namespace"],
                        "Class": td["Name"],
                        "Method": md["Name"],
                        "FQN": f"{td['Namespace']}.{td['Name']}.{md['Name']}",
                        "Doc": self.get_doc(md["CustomAttributes"]),
                    }

    def has_custom_attribute(self, custom_attributes, attr):
        for ca in custom_attributes:
            if ca["Type"] == attr:
                return True
        return False

    def get_doc(self, custom_attributes):
        for ca in custom_attributes:
            if ca["Type"] == "Windows.Win32.Foundation.Metadata.DocumentationAttribute":
                return ca["FixedArguments"][0]["Value"]
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description="API search")
    parser.add_argument("--loglevel", default="INFO")
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, force=True)

    XamlApplication.Start(App)


if __name__ == "__main__":
    main()
