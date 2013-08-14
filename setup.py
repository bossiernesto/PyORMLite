from distutils.core import setup

with open('README.txt') as readme:
    long_description = readme.read()

setup(name="PyORMLite",
    version="0.0.1",
    description="Lightweight ORM for persisting objects",
    long_description=long_description,
    author="Ernesto Bossi",
    author_email="bossi.ernestog@gmail.com",
    url="https://github.com/bossiernesto/PyORMLite",
    license="GPL v3",
    packages=['PyORMLite'],
    package_dir={'PyORMLite': 'PyORMLite'},
    keywords="ORM Lightweight",
    classifiers=["Development Status :: 3 - Alpha",
                 "Topic :: Utilities",
                 "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"]
)