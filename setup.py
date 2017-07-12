from setuptools import setup

from ryoken import __version__


REQUIREMENTS = [
    'pynacl>=1.1.2'
]

PACKAGES = [
    'ryoken'
]

setup(name='ryoken',
      version=__version__,
      url='https://github.com/drakantas/Ryoken',
      description='Token generator and various utilities',
      author='Drakantas',
      license='MIT',
      packages=PACKAGES,
      install_requires=REQUIREMENTS,
      include_package_data=True
)
