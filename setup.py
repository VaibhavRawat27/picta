from setuptools import setup, find_packages

setup(
    name="picta",
    version="0.1.0",
    description="Picta is a Python-first, dependency-free icon library inspired by Lucide Icons. It allows Python developers to easily use SVG icons in web apps, dashboards, or any Python project that can render HTML.",
    author="Vaibhav Rawat",
    packages=find_packages(),
    include_package_data=True,
    package_data={"picta": ["icons/*.svg"]},
    python_requires=">=3.8",
)
