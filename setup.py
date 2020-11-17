from distutils.core import setup
setup(
  name = 'Storer',
  packages = ['Storer'],
  version = '0.5',
  license='MIT',
  description = 'Minimalist storage class for any purpose.',
  author = 'Alexander Kazakov',
  author_email = 'alexander.d.kazakov@gmail.com',
  url = 'https://github.com/AlexanderDKazakov/Storer',
  download_url = 'https://github.com/AlexanderDKazakov/Storer/archive/v0.5.tar.gz',    # I explain this later on
  keywords = ['store', 'pickle'],
  install_requires=[
          'pickle==4.0',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
