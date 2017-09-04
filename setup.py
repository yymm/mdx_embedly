import sys

from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='mdx_embedly',
    version='0.4.0',
    description='Python Markdown extension for embeded url using Embedly',
    long_description=long_description,
    url='https://github.com/yymm/mdx_embedly',
    author='yymm',
    author_email='yuya.yano.6260@gmail.com',
    license='MIT',
    py_modules=['mdx_embedly'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup :: HTML',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='Markdown',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['markdown'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
