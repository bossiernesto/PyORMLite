from distutils.core import setup
import sys


if sys.version_info.major < (3,):
    print("Ristretto is intended for Python 3, please upgrade to any python 3.x version")
    sys.exit(1)

with open('README.txt') as readme:
    long_description = readme.read()

package_name = "ristretto-orm"
ristreto_orm = "risrettoORM"

setup(name=package_name,
      version="0.0.1",
      description="Lightweight ORM for persisting objects for ristretto framework",
      long_description=long_description,
      author="Ernesto Bossi",
      author_email="bossi.ernestog@gmail.com",
      url="https://github.com/bossiernesto/ristretto-orm",
      license="GPL v3",
      packages=[ristreto_orm],
      package_dir={ristreto_orm: ristreto_orm},
      requires=["PyMetabuilder", "mysql-python3", "db-psycopg2", "db-sqlite3"],
      keywords="ORM Lightweight",
      classifiers=["Development Status :: 3 - Alpha",
                   "Topic :: Utilities",
                   "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"]
)
