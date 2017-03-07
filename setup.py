# from ez_setup import use_setuptools
# use_setuptools()

from setuptools import setup, find_packages


entry_points = """
[cosmoscope.plugin]
qt=cosmos_client_qt.main:main
"""

setup(
    name='cosmos-client-qt',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/cosmoscope/cosmos-client-qt',
    license='',
    author='Nicholas Earl',
    author_email='contact@nicholasearl.me',
    description='Front-end qt interface for interacting with the cosmoscope server',
    # install_requires=["cosmoscope"],
    entry_points=entry_points
)