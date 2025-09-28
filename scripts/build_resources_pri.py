import contextlib
import io
import os
import shutil
import subprocess
import tempfile
import urllib.request
import zipfile


def urlget(url):
    with urllib.request.urlopen(url) as f:
        return f.read()


def run(cmd):
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)


def build_resources_pri():
    print("download Microsoft.Windows.SDK.BuildTools")
    nupkg_url = "https://api.nuget.org/v3-flatcontainer/microsoft.windows.sdk.buildtools/10.0.26100.6584/microsoft.windows.sdk.buildtools.10.0.26100.6584.nupkg"
    nupkg = urlget(nupkg_url)

    print("extract bin/10.0.26100.0.x64/makepri.exe")
    with zipfile.ZipFile(io.BytesIO(nupkg)) as zf:
        zf.extract("bin/10.0.26100.0/x64/makepri.exe")

    # FIXME: /Platform (==/pv) is not recognized: Unknown option specified - 'Platform'
    print("create resources.xml with default settings")
    run(["makepri.exe", "createconfig", "/ConfigXml", "resources.xml", "/Default", "en-US", "/pv", "10.0.0"])

    # create resources.pri with empty project root directory
    os.mkdir("root")

    print("create resources.pri from resources.xml")
    run(["makepri.exe", "new", "/ProjectRoot", "root", "/ConfigXml", "resources.xml"])


def main():
    # makepri.exe createconfig /ConfigXml resources.xml /Default en-US /Platform 10.0.0
    # makepri.exe new /ProjectRoot .\root /ConfigXml resources.xml

    print("creating resources.pri")

    with tempfile.TemporaryDirectory() as tmpdir:
        with contextlib.chdir(tmpdir):
            build_resources_pri()
        shutil.copyfile(tmpdir + "\\resources.pri", "resources.pri")


if __name__ == "__main__":
    main()
