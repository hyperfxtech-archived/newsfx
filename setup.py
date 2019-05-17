import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='newsfx',
    version='0.0.3',
    author="HyperFX Tech Team",
    author_email="coffee@hyperfx.tech",
    description="Scraper news article in Viet Nam",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hyperfxtech/newsfx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
