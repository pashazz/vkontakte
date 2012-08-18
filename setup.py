#!/usr/bin/env python3
from distutils.core import setup

version='1.3.2'

setup(
    name='vkontakte',
    version=version,
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['vkontakte'],

    url='http://bitbucket.org/kmike/vkontakte/',
    license = 'MIT license',
    description = "vk.com (aka vkontakte.ru) API wrapper",

    long_description = open('README.rst').read() + open('CHANGES.rst').read(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
