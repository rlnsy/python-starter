import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mathtools",
    version="0.0.1",
    author="Rowan Lindsay",
    author_email="rowan@rowanlindsay.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlnsy/python-starter",
    project_urls={
        "Bug Tracker": "https://github.com/rlnsy/python-starter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "mathtools"},
    packages=setuptools.find_packages(where="mathtools"),
    python_requires=">=3.8",
)
