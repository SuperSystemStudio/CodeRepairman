from setuptools import setup, find_packages

setup(
    name='athena',
    version=1.0,
    long_description=open('README.md').read(),
    author='Mryan',
    author_email='mryan@mryan05.uu.me',
    license='Apache-2.0',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/SuperSystemStudio/CodeRepairwoman',
    py_modules= ['CodeRepairman']
)