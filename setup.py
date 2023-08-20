from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

requirements = [
    "rarfile>=4.0",
    "natsort>=8.4.0",
    "filetype>=1.2.0",
]

setup(
    name="cbx",
    version="0.0.1",
    author="Restil1789",
    author_email="france10004@gmail.com",
    description="Create and maintains cbx.",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Restil1789/cbx",
    project_urls={
        "Bug Tracker": "https://github.com/Restil1789/cbx/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    zip_safe=False
)