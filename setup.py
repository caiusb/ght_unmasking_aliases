from setuptools import setup

setup(name="ght_alias",
    version="0.1",
    description="Unmasking git aliases",
    packages=['alias'],
    dependency_links=['git+git://github.com/caiusb/unicodeManager']
)   
