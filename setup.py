from setuptools import setup

setup(
    name='OceanPython',
    version='1.1',
    packages=[''],
    package_dir={'': 'src'},
    url='https://github.com/Ofwat/OceanPython.git',
    license='',
    author='Niyati.Wawre',
    author_email='niyati.wawre@ofwat.gov.uk',
    description='OceanProject setup file'
)
# setup.py is an integral part of a python package which includes details or information about the files that should be
# a package. This includes the required dependencies for installation and functioning of your Python package, entry points, license, etc.
#
# setup.cfg on the other hand is more about the settings for any plug-ins or the type of distribution you wish to create.
# bdist/sdist and further classification of universal or core-python wheel. It can also be used to configure some meta-data of the setup.py.
