import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="collocation", # Replace with your own username
    version="0.0.6",
    author="Yongfu Liao",
    author_email="liao961120@gmail.com",
    description="Collocation extraction from segmented texts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liao961120/collocation",
    # package_dir = {'': 'src'},
    packages=['collocation'],
    # package_data={
    #     "": ["../data/cilin_tree.json"],
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)