# WinRT xaml api requires "maxversiontested" entry in manifest.
# This script downloads embeddable python package and edit manifest.
# Requires mt.exe which is installed with VisualStudio.

# Download embeddable python package.

if (-not (Test-Path python)) {
    New-Item python -ItemType Directory
}

curl.exe -O https://www.python.org/ftp/python/3.11.3/python-3.11.3-embed-amd64.zip

tar.exe -C python -xzvf python-3.11.3-embed-amd64.zip

# Edit python.exe's manifest for WinRT xaml api.

mt.exe -inputresource:"python\python.exe;#1" -out:python.manifest

(Get-Content -Encoding Ascii python.manifest) | % {
    if ($_ -like "*{e2011457-1546-43c5-a5fe-008deee3d3f0}*") {
        '<maxversiontested Id="10.0.18362.0"/>', $_
    } else {
        $_
    }
} | Set-Content -Encoding Ascii python.manifest

mt.exe -manifest python.manifest -outputresource:"python\python.exe;#1"

# Enable site.

(Get-Content -Encoding Ascii python/python311._pth) | % {
    if ($_ -eq "#import site") {
        "import site"
    } else {
        $_
    }
} | Set-Content -Encoding Ascii python/python311._pth

# Install pip.

curl.exe https://bootstrap.pypa.io/get-pip.py | python\python.exe -

# Install py-win32more.

# FIXME: Automatic build dependency installation doesn't work when using with embeddable python?
python\python.exe -m pip install hatchling

python\python.exe -m pip install -e $PSScriptRoot\..

