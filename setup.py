from setuptools import setup
from setuptools import find_packages
import glob

data_files   = glob.glob('PolyFlow/config/*')
data_files  += glob.glob('PolyFlow/studies/*')

setup(name='PolyFlow', 
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
                        'scikit-learn',
                        'maestrowf',
                        'schema',
                        'patool',
                        'pyunpack',
                        'h5py',
                        'kosh'],
      entry_points = {
          'console_scripts' : ['PolyFlow=PolyFlow.CLI:start_cli']
          },
          data_files=[('share/PolyFlow', data_files)],
          include_package_data=True,
          zip_safe=False)
