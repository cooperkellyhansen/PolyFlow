from setuptools import setup
from setuptools import find_packages
import glob

data_files = glob.glob('/foreman/blueprints/*')

setup(name='polyflow', 
      description='Toolkit for developing microscale fatigue surrogate models',
      classifiers=[
                    'Programming Language :: Python :: 3.11.0'
                    ],
      keywords= 'GPSR',
      packages=find_packages(),
      install_requires=[
                        'tensorflow',
                        'scipy',
                        'numpy',
                        'scikit-learn>=1.0.2',
                        'maestrowf',
                        'schema',
                        'patool',
                        'pyunpack',
                        'h5py',
                        'kosh',
                        'bingo-nasa'],
      entry_points = {
          'console_scripts' : ['polyflow=CLI:start_cli']
          },
          data_files=[('polyflow', data_files)],
          include_package_data=True,
          zip_safe=False)
