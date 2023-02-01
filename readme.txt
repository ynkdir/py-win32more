Python bindings for Win32 API generated from win32metadata.

https://github.com/microsoft/win32metadata

Usage:

> py generate.py json/Windows.Win32.json.xz

How to get latest metadata:

# Download Windows.Win32.winmd
> nuget install -ExcludeVersion -Prerelease Microsoft.Windows.SDK.Win32Metadata

# Generate Windows.Win32.json
> git clone https://github.com/ynkdir/winmd-printer.git
> cd winmd-printer
> dotnet run ..\Microsoft.Windows.SDK.Win32Metadata\Windows.Win32.winmd > ..\Windows.Win32.json
> cd ..

not maintained.
not tested.
