"""Package Setup for Django CodeMirror 6
"""

import pathlib
import re

import setuptools
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox

        errno = tox.cmdline(self.test_args)
        exit(errno)


init = (pathlib.Path('src') / 'django_codemirror6' / '__init__.py').read_text()
match = re.search(r"^__version__ = '(.+)'$", init, re.MULTILINE)
version = match.group(1)

with open('README.rst') as reader:
    readme = reader.read()

setuptools.setup(
    name='django-codemirror6',
    version=version,
    description='Record and replay client web sessions.',
    long_description=readme,
    author='Grant Jenks',
    author_email='contact@grantjenks.com',
    url='https://grantjenks.com/docs/django-codemirror6/',
    license='Apache 2.0',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    install_requires=['Django'],
    project_urls={
        'Documentation': 'https://grantjenks.com/docs/django-codemirror6/',
        'Source': 'https://github.com/grantjenks/django-codemirror6',
        'Tracker': 'https://github.com/grantjenks/django-codemirror6/issues',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
