from setuptools import setup, find_packages
import os

VERSION = '0.0.4'
DESCRIPTION = 'A simple test for launching packages.'

setup(
    name="mypackage1",
    version=VERSION,
    author="Leo Weng",
    author_email="wlaleo@stu.xjtu.edu.cn",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=open('README.md',encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'my package'],
    # data_files=[('cut_video', ['cut_video/clip_to_erase.json'])],
    entry_points={
        'console_scripts': [
            'mypackage1 = mypackage1:main'
        ]
    },
    license="XJTU",
    url="https://github.com/dashboard",
    # scripts=['dist/packagetest'],
    classifiers=[
        "Intended Audience :: All Groups",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
