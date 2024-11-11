from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="chan4kum",
    description="A small package for dvc dl pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chan4kum/DVC_DL_Tensorflow.git",
    author_email="chandankumarsingh1351@gmail.com",
    packages=["src"],
    python_requires=">=3.10",
    install_requires=[
        "dvc",
        "tensorflow[and-cuda]",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3" ,
    ]
)