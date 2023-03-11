from setuptools import setup, find_packages
import generate

generate.build('json/Windows.Win32.json.xz')
setup(
    name="win32more",
    version="0.1",
    packages=find_packages()
)
