from setuptools import setup, find_packages

setup(
    name="picta",
    version="0.1.0",
    description="Python icon library inspired by Lucide",
    author="Vaibhav Rawat",
    packages=find_packages(),
    include_package_data=True,
    package_data={"picta": ["icons/*.svg"]},
    python_requires=">=3.8",
)
