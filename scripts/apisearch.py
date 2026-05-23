# /// script
# dependencies = ["win32more"]
# ///

import asyncio
import io
import itertools
import json
import urllib.request
import zipfile
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from win32more import box_value
from win32more._hstr import hstr
from win32more._map import Map
from win32more._vector import Vector
from win32more.Microsoft.UI.Xaml import FocusState, Window
from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Windows.Foundation.Collections import IMap
from win32more.Windows.Win32.System.WinRT import IInspectable
from win32more.winui3 import XamlApplication, XamlClass

APILIST_CACHE = Path(".apisearch.txt")
LIST_MAX = 200
METADATA_URLS = [
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.2.0/Microsoft.Windows.SDK.Win32Metadata.70.0.11-preview.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.2.0/Microsoft.Windows.WDK.Win32Metadata.0.13.25-experimental.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.2.0/Microsoft.Windows.SDK.Contracts.10.0.26100.7705.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.2.0/Microsoft.WindowsAppSDK.2.0.1.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.2.0/Microsoft.Web.WebView2.1.0.3967.48.zip",
    "https://github.com/ynkdir/winmd-printer/releases/download/v1.2.0/Microsoft.Graphics.Win2D.1.4.0.zip",
]


class App(XamlApplication):
    def OnLaunched(self, args):
        self._search_engine = SearchEngine()
        self._loadpage = LoadPage(self._search_engine)
        self._searchpage = SearchPage(self._search_engine)
        self._window = Window()
        self._window.Title = "Api Search"
        self._window.Activate()
        asyncio.create_task(self._load())

    async def _load(self) -> None:
        self._window.Content = self._loadpage
        await self._loadpage.load()
        self._window.Content = self._searchpage


class LoadPage(XamlClass, Page):
    xaml = """<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">
    <StackPanel HorizontalAlignment="Center">
        <TextBlock>Loading</TextBlock>
        <ListView x:Name="ListView1">
            <ListView.ItemTemplate>
                <DataTemplate>
                    <StackPanel Orientation="Horizontal">
                        <ProgressRing IsActive="True" Visibility="{Binding running}" />
                        <FontIcon Glyph="&#xE001;" Visibility="{Binding done}" /> <!-- check mark -->
                        <TextBlock Text="{Binding name}" />
                    </StackPanel>
                </DataTemplate>
            </ListView.ItemTemplate>
        </ListView>
    </StackPanel>
</Page>"""

    def __init__(self, search_engine: SearchEngine) -> None:
        super().__init__()
        self._search_engine = search_engine
        self.LoadComponentFromString(self.xaml)
        self._items = Vector[IInspectable]()
        self.ListView1.ItemsSource = self._items

    async def load(self) -> None:
        await self._search_engine.load(self)

    def notify_task_start(self, name) -> None:
        m = Map[hstr, IInspectable]()
        m["name"] = name
        m["running"] = True
        m["done"] = False
        self._items.Append(m)

    def notify_task_end(self, name) -> None:
        for m in self._items:
            m = m.as_(IMap[hstr, IInspectable])
            if m["name"].as_(str) == name:
                m["running"] = False
                m["done"] = True
                break


class SearchPage(XamlClass, Page):
    xaml = """<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">
    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
            <RowDefinition Height="Auto"/>
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*"/>
        </Grid.ColumnDefinitions>
        <TextBox x:Name="QueryTextBox" Grid.Row="0" PlaceholderText="Enter API name" TextChanged="QueryTextBox_TextChanged" Loaded="QueryTextBox_Loaded"/>
        <ListView x:Name="ListView1" Grid.Row="1">
            <ListView.ItemTemplate>
                <DataTemplate>
                    <StackPanel Orientation="Horizontal">
                        <TextBlock Visibility="{Binding ModuleMemberVisibility}">
                            <Run Text="{Binding Namespace}" />.<Run Foreground="Tomato" Text="{Binding Member}" />
                        </TextBlock>
                        <TextBlock Visibility="{Binding ClassMemberVisibility}">
                            <Run Text="{Binding Namespace}" />.<Run Foreground="Tomato" Text="{Binding Class}" />.<Run Foreground="Maroon" Text="{Binding Member}" />
                        </TextBlock>
                        <TextBlock Visibility="{Binding DocVisibility}">
                            <Run Text=" " /><Hyperlink NavigateUri="{Binding Doc}">doc</Hyperlink>
                        </TextBlock>
                    </StackPanel>
                </DataTemplate>
            </ListView.ItemTemplate>
        </ListView>
        <StackPanel Grid.Row="2">
            <TextBlock x:Name="Status"></TextBlock>
        </StackPanel>
    </Grid>
</Page>"""

    def __init__(self, search_engine: SearchEngine) -> None:
        super().__init__()
        self._search_engine = search_engine
        self._current_search_task = None
        self.LoadComponentFromString(self.xaml)
        self._items = Vector[IInspectable]()
        self.ListView1.ItemsSource = self._items

    async def QueryTextBox_TextChanged(self, sender, e):
        await self.search(self.QueryTextBox.Text)

    def QueryTextBox_Loaded(self, sender, e):
        self.QueryTextBox.Focus(FocusState.Programmatic)

    async def search(self, query) -> None:
        if self._current_search_task is not None:
            self._current_search_task.cancel()

        self._current_search_task = asyncio.current_task()

        # debouncing
        try:
            await asyncio.sleep(0.3)
        except asyncio.CancelledError:
            return

        if query == "":
            self.clear()
            return

        try:
            matched_api, overflow = await asyncio.to_thread(self._search_engine.search, query, LIST_MAX)
        except asyncio.CancelledError:
            return

        self.update(matched_api, overflow)

        self._current_search_task = None

    def clear(self) -> None:
        self._items.Clear()
        self.Status.Text = ""

    def update(self, items: list, overflow: bool) -> None:
        self._items.ReplaceAll(
            [Map[hstr, IInspectable]({k: box_value(v) for k, v in self.make_item(api).items()}) for api in items]
        )
        if overflow:
            self.Status.Text = f"... (over {LIST_MAX})"

    def make_item(self, api: dict) -> dict:
        dto = {
            "DocVisibility": False,
            "Doc": "",
            "ModuleMemberVisibility": False,
            "ClassMemberVisibility": False,
            "Namespace": "",
            "Class": "",
            "Member": "",
        }
        if api["Doc"] is not None:
            dto["DocVisibility"] = True
            dto["Doc"] = api["Doc"]
        if "Method" in api:
            dto["ClassMemberVisibility"] = True
            dto["Namespace"] = api["Namespace"]
            dto["Class"] = api["Class"]
            dto["Member"] = api["Method"]
        elif "Field" in api:
            dto["ClassMemberVisibility"] = True
            dto["Namespace"] = api["Namespace"]
            dto["Class"] = api["Class"]
            dto["Member"] = api["Field"]
        else:
            dto["ModuleMemberVisibility"] = True
            dto["Namespace"] = api["Namespace"]
            dto["Member"] = api["Name"]
        return dto


class SearchEngine:
    def __init__(self):
        self._apilist = []

    async def load(self, observer) -> None:
        def run_in_thread(name, fun, *args):
            observer.notify_task_start(name)
            task = asyncio.create_task(asyncio.to_thread(fun, *args))
            task.add_done_callback(lambda _: observer.notify_task_end(name))
            return task

        if APILIST_CACHE.exists():
            self._apilist = await run_in_thread("reading cache file", lambda: json.loads(APILIST_CACHE.read_text()))
            return

        tasks = []
        for url in METADATA_URLS:
            tasks.append(run_in_thread(f"downloading {url}", MetadataLoader().load, url))
        meta = list(itertools.chain.from_iterable(await asyncio.gather(*tasks)))

        self._apilist = await run_in_thread("generating api list", ApiListGenerator().generate, meta)

        await run_in_thread("writing cache file", lambda: APILIST_CACHE.write_text(json.dumps(self._apilist)))

    def search(self, query: str, max_length: int) -> tuple[list[dict], bool]:
        r = []
        query = query.lower()
        for api in self._apilist:
            if query in api["FQN_lower"]:
                r.append(api)
                if len(r) == max_length:
                    return r, True
        return r, False


class MetadataLoader:
    def download(self, url: str) -> bytes:
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

    def load(self, url: str) -> list[Any]:
        return [td for td in self.download_metadata(url) if self.is_public(td)]

    def is_public(self, td: Any) -> bool:
        is_winrt = "WindowsRuntime" in td["Attributes"]
        if is_winrt:
            return td["Namespace"] != "" and td["BaseType"] != "System.Attribute"
        else:
            return td["Namespace"] != "" and "Public" in td["Attributes"]


class ApiListGenerator:
    def generate(self, meta: list[Any]):
        return list(self.enumerate_name_with_lower_fqn(meta))

    def enumerate_name_with_lower_fqn(self, meta: list[Any]) -> Iterable[dict]:
        for api in self.enumerate_name(meta):
            api["FQN_lower"] = api["FQN"].lower()
            yield api

    def enumerate_name(self, meta: list[Any]) -> Iterable[dict]:
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
    XamlApplication.Start(App)


if __name__ == "__main__":
    main()
