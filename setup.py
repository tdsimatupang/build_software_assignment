from setuptools import setup, find_packages

setup(
    name="Asteroids_NeoWs",
    version="0.1.0",
    author="Tulus Daniel Simatupang",
    author_email="tdsimatupang@gmail.com",
    description="Searching for Asteroids based on their closest approach date to Earth",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tdsimatupang/build_software_assignment",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.11.0',
    install_requires=[
        "requests",
        "pyyaml",
        "matplotlib",
        "plyer"
    ],
)
