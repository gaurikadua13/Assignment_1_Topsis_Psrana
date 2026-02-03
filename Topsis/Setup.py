from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="topsis-gaurika-dua-102303271",
    version="1.0.1",
    author="Gaurika Dua 102303271",
    author_email="gdua_be23@thapar.edu",
    description="TOPSIS (MCDM) implementation for ranking alternatives using multiple criteria.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "topsis-gaurika-dua-102303271=topsis_gaurika_dua_102303271.cli:main"
        ]
    },
)
