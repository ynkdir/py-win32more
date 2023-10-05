Python bindings for Win32 API generated from win32metadata.

https://github.com/microsoft/win32metadata

Usage:

> py generate.py json/Windows.Win32.json.xz

# Generate one file module for specific api set.
> py generate.py -s selector.txt -o win32.py json/Windows.Win32.json.xz

selector.txt format is:

# namespace
Windows.Win32.System.Com
# fullname
Windows.Win32.UI.WindowsAndMessaging.MessageBoxW
# just name
CreateFileW
MB_OK


How to get latest metadata:

# Download Windows.Win32.winmd
> nuget install -ExcludeVersion -Prerelease Microsoft.Windows.SDK.Win32Metadata

# Generate Windows.Win32.json
> git clone https://github.com/ynkdir/winmd-printer.git
> cd winmd-printer
> dotnet run ..\Microsoft.Windows.SDK.Win32Metadata\Windows.Win32.winmd > ..\Windows.Win32.json
> cd ..
