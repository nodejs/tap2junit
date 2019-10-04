from os import path

import setuptools

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md")) as in_file:
    long_description = in_file.read()

setuptools.setup(
    name="tap2junit",
    version="0.1.5",
    description="Tap13 to jUnit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nodejs/tap2junit",
    author="Node.js contributors",
    author_email="cclauss@me.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License, Version 2.0",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords="tap13 junit",
    packages=["tap2junit"],
    install_requires=["junit-xml", "yamlish"],
    entry_points={"console_scripts": ["tap2junit = tap2junit.__main__:main"]},
)
