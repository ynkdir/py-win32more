from setuptools import setup, find_packages
import generate

generate.main()
setup(
    name="win32more",
    version="0.1",
    packages=find_packages()
)
