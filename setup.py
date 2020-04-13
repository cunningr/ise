from setuptools import find_packages, setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ISE',
    version='1.1.0',
    py_modules=['ise'],
    url='https://github.com/falkowich/ise',
    download_url='https://pypi.python.org/pypi/ise',
    license='LICENSE.md',
    maintainer='Andreas Falk',
    maintainer_email='falk@sadsloth.net',
    description='Python module to manage Cisco ISE via the ERS API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'furl>=2.1.0',
        'requests>=2.23.0'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage'
        ],
    },
)
