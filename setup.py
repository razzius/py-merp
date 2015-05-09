#!/usr/bin/env python

from distutils.core import setup
setup(name='py-merp',
      version='0.0.2',
      py_modules = ['merp'],
      package_dir = {'': 'src'},
      requires = ['numpy', 'scipy', 'matplotlib', 'requests'],
      description='mendelian randomization pipeline',
      long_description='py-merp',
      author='Peter Yin',
      author_email='py.peteryin@gmail.com',
      url='http://github.com/py-merp',
      license='',
      platforms='any that supports python 2.7',
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Education',
            'Intended Audience :: Science and Research',
            'Intended Audience :: Developers',
            #'License :: OSI Approved :: MIT',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: POSIX :: SunOS/Solaris',
            'Operating System :: Unix',
            'Programming Language :: Python :: 2.7',
            'Topic :: Scientific/Engineering :: Bioinformatics',
            'Topic :: Scientific/Engineering :: Genetics',
            'Topic :: Medicine :: Epidemiology',
            ],
      )
