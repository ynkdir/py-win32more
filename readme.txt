Python bindings for Win32 API generated from win32metadata.

https://github.com/microsoft/win32metadata

TO GENERATE:

# Download Windows.Win32.winmd
> nuget.exe install Microsoft.Windows.SDK.Win32Metadata -Version 39.0.18-preview

# Generate Windows.Win32.json
> git clone https://github.com/ynkdir/winmd-printer.git
> cd winmd-printer
> dotnet run ..\Microsoft.Windows.SDK.Win32Metadata.39.0.18-preview\Windows.Win32.winmd > ..\Windows.Win32.json
> cd ..

# Generate Python code
> py generate.py Windows.Win32.json

not maintained.
not tested.
