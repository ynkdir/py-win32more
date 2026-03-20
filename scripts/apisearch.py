# /// script
# dependencies = ["win32more"]
# ///

import argparse
import asyncio
import concurrent.futures
import io
import itertools
import json
import logging
import urllib.request
import zipfile
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from win32more import box_value
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

        self._ready = False
        self._search_engine = SearchEngine()
        self._current_search_task = None

        asyncio.create_task(self._load())

    async def _load(self) -> None:
        self.ListView1.Items.Append(
            XamlLoader.Load(
                self,
                """<TextBlock xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation">loading</TextBlock>""",
            )
        )
        self.ListView1.Items.Append(
            XamlLoader.Load(
                self,
                """<ProgressBar xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" IsIndeterminate="True" />""",
            )
        )

        await asyncio.to_thread(self._search_engine.load)

        self._ready = True

        if self.TextBlock1.Text != "":
            await self._search()
            return

        self.ListView1.Items.Clear()
        self.ListView1.Items.Append(
            XamlLoader.Load(
                self,
                """<TextBlock xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation">ready</TextBlock>""",
            )
        )

    async def _search(self) -> None:
        if not self._ready:
            return

        if self._current_search_task is not None:
            self._current_search_task.cancel()

        self._current_search_task = asyncio.current_task()

        query = self.TextBlock1.Text
        items = self.ListView1.Items

        # debouncing
        try:
            await asyncio.sleep(0.3)
        except asyncio.CancelledError:
            return

        if query == "":
            items.Clear()
            return

        try:
            matched_api = await asyncio.to_thread(self._search_engine.search, query)
        except asyncio.CancelledError:
            return

        r = []
        for i, api in enumerate(matched_api):
            r.append(self.make_item(api))
            if i == LIST_MAX:
                r.append(box_value(f"... (over {LIST_MAX})"))
                break
        items.ReplaceAll(r)

        self._current_search_task = None

    def make_item(self, api: Any) -> object:
        if api["Doc"] is None:
            link = ""
        else:
            link = f"""<Hyperlink NavigateUri="{api["Doc"]}">doc</Hyperlink>"""
        if "Method" in api:
            item = f"{api['Namespace']}.<Run Foreground='Tomato'>{api['Class']}</Run>.<Run Foreground='Maroon'>{api['Method']}</Run> {link}"
        elif "Field" in api:
            item = f"{api['Namespace']}.<Run Foreground='Tomato'>{api['Class']}</Run>.<Run Foreground='Maroon'>{api['Field']}</Run> {link}"
        else:
            item = f"{api['Namespace']}.<Run Foreground='Tomato'>{api['Name']}</Run> {link}"
        xaml = f'<TextBlock xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation">{item}</TextBlock>'
        return XamlLoader.Load(self, xaml)

    async def TextBlock1_TextChanged(self, sender, e):
        await self._search()

    def TextBlock1_Loaded(self, sender, e):
        self.TextBlock1.Focus(FocusState.Programmatic)


class SearchEngine:
    def __init__(self):
        self._apilist = []

    def load(self) -> None:
        if APILIST_CACHE.exists():
            self._apilist = json.loads(APILIST_CACHE.read_text())
        else:
            meta = MetadataLoader().load()
            self._apilist = ApiListGenerator().generate(meta)
            logger.info(f"writing cache file {APILIST_CACHE}")
            APILIST_CACHE.write_text(json.dumps(self._apilist))

    def search(self, query: str) -> list[Any]:
        r = []
        query = query.lower()
        for api in self._apilist:
            if query in api["FQN_lower"]:
                r.append(api)
        return r


class MetadataLoader:
    def download(self, url: str) -> bytes:
        logger.info(f"download: {url}")
        with urllib.request.urlopen(url) as f:
            return f.read()

    def download_zip(self, url: str) -> zipfile.ZipFile:
        data = self.download(url)
        file = io.BytesIO(data)
        return zipfile.ZipFile(file)

    def download_metadata(self, url: str) -> Iterable[Any]:
        zfile = self.download_zip(url)
        for zname in zfile.namelist():
            zpath = zipfile.Path(zfile, zname)
            yield from json.loads(zpath.read_text())

    def load(self) -> list[Any]:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            return list(
                itertools.chain.from_iterable(
                    executor.map(
                        lambda url: [td for td in self.download_metadata(url) if self.is_public(td)], METADATA_URLS
                    )
                )
            )

    def is_public(self, td: Any) -> bool:
        is_winrt = "WindowsRuntime" in td["Attributes"]
        if is_winrt:
            return td["Namespace"] != "" and td["BaseType"] != "System.Attribute"
        else:
            return td["Namespace"] != "" and "Public" in td["Attributes"]


class ApiListGenerator:
    def generate(self, meta: list[Any]):
        logger.info("generating api list")
        return list(self.enumerate_name_with_lower_fqn(meta))

    def enumerate_name_with_lower_fqn(self, meta: list[Any]) -> Iterable[str]:
        for api in self.enumerate_name(meta):
            api["FQN_lower"] = api["FQN"].lower()
            yield api

    def enumerate_name(self, meta: list[Any]) -> Iterable[str]:
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
