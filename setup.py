import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="koekiemonster",
    version="0.0.1",
    author="Glenn Wilkinson",
    author_email="glennzw@protonmail.com",
    description="Koekie Monster loads cookies from FireFox, allowing you to easily use your session cookies programatically.",
    url="https://github.com/glennzw/koekiemonster",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
