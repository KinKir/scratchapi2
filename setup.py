from setuptools import setup, find_packages

with open("README", "r") as f:
    longdesc = f.read()

setup(
    name="scratchapi2",
    version="0.1",
    description="The New Scratch API Client.",
    long_description=longdesc,
    url="https://github.com/apple502j/scratchapi2",
    author="Apple502j",
    license="GPLv3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Natural Language :: Japanese",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords="scratch api requests",
    packages=find_packages(),
    install_requires="requests",
    python_requires=">=3.5"
    )
