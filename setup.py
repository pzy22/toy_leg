from setuptools import find_packages
from distutils.core import setup


setup(
    name='go2_gym',
    version='0.0.1',
    author='Shining',
    license="BSD-3-Clause",
    packages=find_packages(),
    author_email='zsmpzy20319@gmail.com',
    description='A Unitree Go2 Gym Environment for reinforcement learning',
    install_requires=['matplotlib']
)