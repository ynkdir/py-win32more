Python bindings for Win32 API generated from win32metadata.

https://github.com/microsoft/win32metadata

TO GENERATE:

# Download Windows.Win32.winmd
> nuget install -ExcludeVersion -Prerelease Microsoft.Windows.SDK.Win32Metadata

# Generate Windows.Win32.json
> git clone https://github.com/ynkdir/winmd-printer.git
> cd winmd-printer
> dotnet run ..\Microsoft.Windows.SDK.Win32Metadata\Windows.Win32.winmd > ..\Windows.Win32.json
> cd ..

# Generate Python code
> py generate.py Windows.Win32.json

not maintained.
not tested.
