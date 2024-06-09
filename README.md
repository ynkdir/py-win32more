# Win32more

[![PyPI - Version](https://img.shields.io/pypi/v/win32more.svg)](https://pypi.org/project/win32more)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/win32more.svg)](https://pypi.org/project/win32more)

Win32more is a python bindings for Windows API generated from metadata.

https://github.com/microsoft/win32metadata

https://www.nuget.org/packages/Microsoft.Windows.SDK.Contracts

https://github.com/microsoft/WindowsAppSDK

## Installation

```console
pip install win32more
```

## Usage

```pycon
>>> from win32more.Windows.Win32.UI.WindowsAndMessaging import MessageBox, MB_OK
>>> MessageBox(0, "hello, world", "win32more", MB_OK)
```
