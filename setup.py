import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

# This call to setup() does all the work
setuptools.setup(
    name="python-unittests-example",
    version="0.0.1-SNAPSHOT",
    description="Python unit tests example project ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CGnal/python-unittests-example",
    author="Nicola Romeo Arena",
    author_email="nromeoarena@cgnal.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
)