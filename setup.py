import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv_to_geojson",
    version="0.0.1",
    author="Miquel Vande Velde",
    author_email="miquel.vandevelde@gmail.com",
    description="Converts csv files to geojson points.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miquel-vv/csv-to-geojson",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'geojson'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['csv_to_geojson=csv_to_geojson.command_line:main']
    }
)