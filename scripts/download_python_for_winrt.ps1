# WinRT xaml api requires "maxversiontested" entry in manifest.
# This script downloads embeddable python package and edit manifest.

$version = "3.11.3"
$arch = "amd64"
$python_embed_url = "https://www.python.org/ftp/python/$version/python-$version-embed-$arch.zip"
$tcltk_url = "https://www.python.org/ftp/python/$version/$arch/tcltk.msi"
$buildtools_url = "https://globalcdn.nuget.org/packages/microsoft.windows.sdk.buildtools.10.0.22621.1.nupkg"
$mt_exe = ".\buildtools\bin\10.0.22621.0\x64\mt.exe"

Write-Host "Download enbeddable python package." -ForegroundColor Green

Invoke-WebRequest $python_embed_url -OutFile python.zip

Expand-Archive python.zip -DestinationPath python

Write-Host "Download mt.exe" -ForegroundColor Green

Invoke-WebRequest $buildtools_url -OutFile buildtools.zip

Expand-Archive buildtools.zip -DestinationPath buildtools

Write-Host "Edit python.exe's manifest for WinRT xaml api." -ForegroundColor Green

& $mt_exe -inputresource:"python\python.exe;#1" -out:python.manifest

(Get-Content python.manifest) -replace '.*{e2011457-1546-43c5-a5fe-008deee3d3f0}.*', "<maxversiontested Id=`"10.0.18362.0`"/>`r`n`$0" | Set-Content python.manifest

& $mt_exe -manifest python.manifest -outputresource:"python\python.exe;#1"

Write-Host "Enable site and Lib." -ForegroundColor Green

(Get-Content python/python311._pth) -replace "^\.$", "Lib`r`n." -replace '^#import site$', 'import site' | Set-Content python/python311._pth
New-Item python\Lib -ItemType Directory

Write-Host "Install pip." -ForegroundColor Green

(Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py).Content | python\python.exe -

Write-Host "Install tkinter" -ForegroundColor Green

Invoke-WebRequest $tcltk_url -OutFile tcltk.msi
Start-Process msiexec.exe "/a tcltk.msi targetdir=`"$PWD\__tmp`" /qn" -Wait
Move-Item __tmp\DLLs\* python\
Move-Item __tmp\Lib\* python\Lib\
Move-Item __tmp\tcl python\
Remove-Item -Recurse __tmp

Write-Host "Install py-win32more." -ForegroundColor Green

# FIXME: Automatic build dependency installation doesn't work when using with embeddable python?
python\python.exe -m pip install hatchling

python\python.exe -m pip install -e $PSScriptRoot\..

Write-Host "python\python.exe is ready." -ForegroundColor Green
