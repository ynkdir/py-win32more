from setuptools import setup, find_packages
import generate
import generatert

generate.build('json/Windows.Win32.json.xz')
generatert.build('json/Windows.WinRT.json.xz')
setup(
    name="win32more",
    version="0.4",
    packages=find_packages()
)
