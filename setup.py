try:
    import setuptools
except ImportError:
    print("Can't import SetupTools from STDLib. Please install it first!")
"""
    ZypeLang - A OpenSource, easy-to-use, easy-to-read & easy-to-write replacement of JSON based on Python.
"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ZypeSDK",
    version="1.5",
    author="TechGeeks",
    author_email="ZypeSDK@tgeeks.cf",
    maintainer="Rajdeep Malakar",
    maintainer_email="Rajdeep@tgeeks.cf",
    description="Zype Language SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zype-Z/ZypeLang",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points=dict(
        console_scripts=['zyper=ZypeSDK.__init__:Main']
    )
)
