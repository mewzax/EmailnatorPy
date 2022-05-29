import os
from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='SmartnatorPy',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='📮 A simple wrapper for Smartnator (old. Gmailnator) to get unlimited gmail written in Python',
    keywords='temp mail tempmail smartnator.com',
    url='https://github.com/Mewzax/SmartnatorPy',
    author='Mewzax',
    author_email='mewdev@pm.me',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)