from setuptools import setup
import os

os.system("touch /tmp/test")  # Executes remote shell script

setup(
    name="rsac-demo-package",
    version="0.1",
    packages=["rsac_demo"],
    install_requires=[],
)
