import os
from setuptools import setup, find_packages


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            # Generate the path relative to the package
            rel_path = os.path.relpath(os.path.join(path, filename), directory)
            # Replace the directory base in the relative path with the correct package path
            package_path = os.path.join('gita_fastapi/app', rel_path)
            paths.append(package_path)
    return paths

# Walk the static and template directories to ensure contents included recursively
static_files = package_files('gita_fastapi/app/static')
template_files = package_files('gita_fastapi/app/templates')


def read_version():
    with open('gita_fastapi/__metadata__.py', 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]

    raise RuntimeError("Unable to find version string.")

version = read_version()

# Read README for long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements_file = "requirements/base.txt"

# Read requirements/base.txt for install_requires
with open(requirements_file, encoding="utf-8") as f:
    install_requires = f.read().splitlines()

with open("requirements/latest.txt", encoding="utf-8") as f:
    install_extras_latest= f.read().splitlines()

# with open("requirements/data.txt", encoding="utf-8") as f:
#     install_extras_data = f.read().splitlines()

# with open("requirements/postgres.txt", encoding="utf-8") as f:
#     install_extras_postgres = f.read().splitlines()

# with open("requirements/mariadb.txt", encoding="utf-8") as f:
#     install_extras_mariadb = f.read().splitlines()

# with open("requirements/saml.txt", encoding="utf-8") as f:
#     install_extras_saml = f.read().splitlines()

setup(
    name='gita_fastapi',
    version=version,
    url='https://github.com/signebedi/gita-fastapi',
    author='Sig Janoska-Bedi',
    author_email='signe@atreeus.com',
    description=' a general text search and reference tool written using FastAPI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'gitactl=gita_fastapi.cli.__init__:cli',
        ],
    },
    # 
    include_package_data=True,
    package_data={
        'gita_fastapi.app': static_files + template_files,
    },
    extras_require={
        "latest": install_extras_latest,
        # "data": install_extras_data,
        # "postgres": install_extras_postgres,
        # "mariadb": install_extras_mariadb,
        # "saml": install_extras_saml,
    },
)
