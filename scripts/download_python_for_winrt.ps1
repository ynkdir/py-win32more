# WinRT xaml api requires "maxversiontested" entry in manifest.
# This script downloads embeddable python package and edit manifest.
# Requires mt.exe which is installed with VisualStudio.

# Download embeddable python package.

$version = "3.11.3"
$arch = "amd64"
$python_embed_url = "https://www.python.org/ftp/python/$version/python-$version-embed-$arch.zip"
$tcltk_url = "https://www.python.org/ftp/python/$version/$arch/tcltk.msi"

Invoke-WebRequest $python_embed_url -OutFile "python-$version-embed-$arch.zip"

Expand-Archive python-$version-embed-$arch.zip -DestinationPath python

# Edit python.exe's manifest for WinRT xaml api.

mt.exe -inputresource:"python\python.exe;#1" -out:python.manifest

(Get-Content python.manifest) -replace '.*{e2011457-1546-43c5-a5fe-008deee3d3f0}.*', "<maxversiontested Id=`"10.0.18362.0`"/>`r`n`$0" | Set-Content python.manifest

mt.exe -manifest python.manifest -outputresource:"python\python.exe;#1"

# Enable site and Lib.

(Get-Content python/python311._pth) -replace "^\.$", "Lib`r`n." -replace '^#import site$', 'import site' | Set-Content python/python311._pth
New-Item python\Lib -ItemType Directory

# Install pip.

(Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py).Content | python\python.exe -

# Install tkinter

Invoke-WebRequest $tcltk_url -OutFile tcltk.msi
Start-Process msiexec.exe "/a tcltk.msi targetdir=`"$PWD\__tmp`" /qn" -Wait
Move-Item __tmp\DLLs\* python\
Move-Item __tmp\Lib\* python\Lib\
Move-Item __tmp\tcl python\
Remove-Item -Recurse __tmp

# Install py-win32more.

# FIXME: Automatic build dependency installation doesn't work when using with embeddable python?
python\python.exe -m pip install hatchling

python\python.exe -m pip install -e $PSScriptRoot\..

