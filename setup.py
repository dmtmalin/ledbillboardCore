#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

sys.path.insert(0, 'src')

requires = [
    'Django==1.11',
    'django-grappelli==2.9.1',
    'django-webdav-storage==0.6.1',
    'graphene-django==1.3',
    'django-filter==1.0.2',
    'psycopg2==2.7.1',
]

setup(
    name='ledbillboard',
    version='0.0.1',
    keywords='web django',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    license='',
    author='dmt',
    author_email='',
    description='',
    zip_safe=False,
    include_package_data=True,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'ledbillboard = ledbillboard.manage:main',
        ]
    },
)
