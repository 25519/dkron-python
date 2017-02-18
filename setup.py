from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='dkron-cli',
    description='Command line interface client for Dkron',
    author='Paweł Olejniczak',
    author_email='pawel.olejniczak@gmail.com',
    url='https://github.com/Eyjafjallajokull/dkron-cli',
    license='BSD',
    long_description=long_description,
    version=__version__,
    download_url='https://github.com/Eyjafjallajokull/dkron-cli/tarball/' + __version__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points={
        'console_scripts': [
            'dkron-cli=dkron_cli.__main__:main'
        ]
    },
)