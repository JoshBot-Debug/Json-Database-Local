import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonDB",
    version="0.0.1",
    author="Joshua Joseph Myers",
    author_email="JoshuaMyersWebDev@gmail.com",
    description="This is a local json database, the json file it creates can be managed using this package and then uploaded online for your React.js static website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoshBot-Debug/Json-Database-Local",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
