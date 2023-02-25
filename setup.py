#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the imagedownloader"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_Description = f.read()
    
setup(
    name = "imagedownloader",
    author = "Mazhar",
    author_email = "mazqoty.01@gmail.com",
    maintainer = "Mazhar",
    maintainer_email = "mazqoty.01@gmail.com",
    version = "1.0.3",
    url = "https://github.com/mm-mazhar/imagedownloader.git",
    download_url = "https://github.com/mm-mazhar/imagedownloader.git",
    project_urls = {"Bug Tracker": "https://github.com/mm-mazhar/imagedownloader/issues"},
    keywords = ["Download Images", "Get Images", "Python", "ImageDownloader", "Python Package", "Downloads"],
    license = "BSD",
    description = "Python Package to Download Images", 
    #long_description = "Python Package to Download Images",
    long_description = long_Description,
    long_description_content_type = "text/markdown",
    python_requires = ">=3.7",
    include_package_data = True,
    packages = find_packages(),
    install_requires = ["requests==2.27.1", 
                        "setuptools==65.6.3"],
    classifiers = [
        #"Environment :: Web Environment",
        #"Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    # entry_points = {
    #     "console_scripts" : [
    #         "login = lib_work_login.__main__:main",
    #         "configure = lib_work_login.__main__:configure",
    #     ]
    # },
    # setup_requires  = ["pytest-runner"],
    # tests_require = ["pytest"],
    
)