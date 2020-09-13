import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="npy3d",
    version="0.0.1-rc1",
    author="Hirotsugu Daba",
    description="A Python library for 3D vector and matrix operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dabasan/npy3d",
    packages=setuptools.find_packages("src"),
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
