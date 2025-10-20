# How to create packaged application

Some specific API (e.g. [Windows AI API](https://learn.microsoft.com/en-us/windows/ai/apis/troubleshooting)) requires package identity at runtime.

You need to make your application packaged.

See [Generating MSIX package components](https://learn.microsoft.com/en-us/windows/msix/desktop/desktop-to-uwp-manual-conversion)

# 1. Download standalone python package

```powershell
> pymanager install --target=testapp
# install win32more
> testapp/python.exe -m pip install -r test_requirements.txt
```

If you want to create self-contained package.  Use scripts/build_selfcontained.py.

```powershell
> py scripts/build_selfcontained.py --target=testapp
```

# 2. Move to package directory

```powershell
> cd testapp
```

# 3. Create AppxManifest.xml

For example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Package
    xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
    xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"
    xmlns:uap5="http://schemas.microsoft.com/appx/manifest/uap/windows10/5"
    xmlns:uap10="http://schemas.microsoft.com/appx/manifest/uap/windows10/10"
    xmlns:desktop4="http://schemas.microsoft.com/appx/manifest/desktop/windows10/4"
    xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
    xmlns:systemai="http://schemas.microsoft.com/appx/manifest/systemai/windows10"
    IgnorableNamespaces="uap rescap systemai desktop4">

    <Identity Name="Win32more.TestApp" Version="1.0.0.0" Publisher="CN=CommonName, O=Organization, L=City, S=State, C=Country" ProcessorArchitecture="x64" />

    <Properties>
        <DisplayName>Win32more.TestApp</DisplayName>
        <PublisherDisplayName>Win32more</PublisherDisplayName>
        <Description>TestApp</Description>

        <!-- TODO: create your logo and save to target directory -->
        <Logo>logo.png</Logo>

    </Properties>

    <Resources>
        <Resource Language="en-us" />
    </Resources>

    <Dependencies>
        <TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.17763.0" MaxVersionTested="10.0.26226.0" />

        <!-- Specify your dependency.  Remove this line for self-contained package. -->
        <PackageDependency Name="Microsoft.WindowsAppRuntime.1.8" MinVersion="8000.0.0.0" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" />

    </Dependencies>

    <Capabilities>
        <rescap:Capability Name="runFullTrust"/>
        <systemai:Capability Name="systemAIModels"/>
    </Capabilities>

    <Applications>
        <Application
                Id="TestApp"
                Executable="python.exe"
                EntryPoint="Windows.FullTrustApplication"
                uap10:RuntimeBehavior="packagedClassicApp"
                uap10:TrustLevel="mediumIL">
            <uap:VisualElements
                DisplayName="TestApp"
                Description="TestApp"
                BackgroundColor="#464646"
                Square150x150Logo="logo.png"
                Square44x44Logo="logo.png"
                />
            <Extensions>
                <uap5:Extension Category="windows.appExecutionAlias">
                    <uap5:AppExecutionAlias desktop4:Subsystem="windows">
                        <uap5:ExecutionAlias Alias="testapp.exe" />
                    </uap5:AppExecutionAlias>
                </uap5:Extension>
            </Extensions>
        </Application>
    </Applications>

</Package>
```

# 4. Install package

[You need to enable Developer Mode on Windows11.](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development)

```powershell
> Add-AppxPackage -Register AppxManifest.xml
```

# 5. Get package information
```powershell
> Get-AppxPackage | ? { $_.Name -eq "Win32more.TestApp" }

Name              : Win32more.TestApp
Publisher         : CN=CommonName, O=Organization, L=City, S=State, C=Country
Architecture      : X64
ResourceId        :
Version           : 1.0.0.0
PackageFullName   : Win32more.TestApp_1.0.0.0_x64__x22gc0rg6bp3w
InstallLocation   : C:\Users\yukih\work\py-win32more\testapp
IsFramework       : False
PackageFamilyName : Win32more.TestApp_x22gc0rg6bp3w
PublisherId       : x22gc0rg6bp3w
IsResourcePackage : False
IsBundle          : False
IsDevelopmentMode : True
NonRemovable      : False
IsPartiallyStaged : False
SignatureKind     : None
Status            : Ok
```

# 6. Get package AppID

```powershell
> Get-StartApps | ? { $_.Name -eq "TestApp" }

Name    AppID
----    -----
TestApp Win32more.TestApp_x22gc0rg6bp3w!TestApp
```

# 7. Start TestApp

You can now start testapp.exe.

```powershell
> testapp.exe
Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from win32more import Char, UInt32
>>> from win32more.Windows.Win32.Storage.Packaging.Appx import GetCurrentPackageFullName
>>> buf = (Char * 1024)()
>>> length = UInt32(1024)
>>> GetCurrentPackageFullName(length, buf)
0
>>> buf.value
'Win32more.TestApp_1.0.0.0_x64__x22gc0rg6bp3w'
```

# 8. Uninstall TestApp

```powershell
> Remove-AppxPackage Win32more.TestApp_1.0.0.0_x64__x22gc0rg6bp3w
```
