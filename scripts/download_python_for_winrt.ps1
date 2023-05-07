# WinRT xaml api requires "maxversiontested" entry in manifest.
# This script downloads embeddable python package and edit manifest.
# Requires mt.exe which is installed with VisualStudio.

# Download embeddable python package.

Invoke-WebRequest https://www.python.org/ftp/python/3.11.3/python-3.11.3-embed-amd64.zip -OutFile python-3.11.3-embed-amd64.zip

Expand-Archive python-3.11.3-embed-amd64.zip -DestinationPath python

# Edit python.exe's manifest for WinRT xaml api.

mt.exe -inputresource:"python\python.exe;#1" -out:python.manifest

(Get-Content python.manifest) -replace '^.*{e2011457-1546-43c5-a5fe-008deee3d3f0}.*$', "<maxversiontested Id=`"10.0.18362.0`"/>`r`n`$0" | Set-Content python.manifest

mt.exe -manifest python.manifest -outputresource:"python\python.exe;#1"

# Enable site.

(Get-Content python/python311._pth) -replace '^#import site$', 'import site' | Set-Content python/python311._pth

# Install pip.

(Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py).Content | python\python.exe -

# Install py-win32more.

# FIXME: Automatic build dependency installation doesn't work when using with embeddable python?
python\python.exe -m pip install hatchling

python\python.exe -m pip install -e $PSScriptRoot\..

