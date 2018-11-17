import os
import setuptools

setuptools.setup(
    name='package-demo',
    version='0.0.1',
    author='newnewcoder',
    author_email='pinkycho1221@gmail.com',
    keywords='package demo',
    description='This is a package demo.',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    url='https://github.com/newnewcoder/pypi-package-demo',
    packages=setuptools.find_packages(),
    license='MIT'
)