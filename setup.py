from distutils.core import setup
from setuptools import find_packages


setup(
  name         = 'storer',
  packages     = find_packages("src"),
  package_dir  = {"": "src"},
  version      = '0.9.5',
  license      = 'MIT',
  description  = 'Minimalist storage class for any purpose.',
  author       = 'Alexander D. Kazakov',
  author_email = 'alexander.d.kazakov@gmail.com',
  url          = 'https://github.com/AlexanderDKazakov/Storer',
  download_url = 'https://github.com/AlexanderDKazakov/Storer/archive/v0.9.5.tar.gz',
  keywords     = ['store', 'pickle'],
  install_requires=[
          '',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
