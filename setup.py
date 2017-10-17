"""
  Pythia Mill
"""

from setuptools import setup, find_packages, Extension

from codecs import open
import os
import os.path as osp
import numpy as np

def get_includes():
  env = os.environ

  includes = []

  for k in ['CPATH', 'C_INCLUDE_PATH', 'INCLUDE_PATH']:
    if k in env:
      includes.append(env[k])

  return includes

from Cython.Build import cythonize

here = osp.abspath(osp.dirname(__file__))

with open(osp.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

extra_compile_args=['-std=c++11', '-O3', '-D_GLIBCXX_USE_CXX11_ABI=0']

extensions = [
  Extension(
    'pythiamill.utils.detector', ['pythiamill/utils/detector.pyx'],
    libraries=['stdc++', 'pythia8'],
    include_dirs=[np.get_include()] + get_includes(),
    language='c++',
    extra_compile_args=extra_compile_args
  ),
  Extension(
    'pythiamill.utils.pythiautils', ['pythiamill/utils/pythiautils.pyx'],
    libraries=['stdc++', 'pythia8'],
    include_dirs=[np.get_include()] + get_includes(),
    language='c++',
    extra_compile_args=extra_compile_args
  ),

  Extension(
    'pythiamill.utils.sdetector', ['pythiamill/utils/sdetector.pyx'],
    libraries=['stdc++', 'pythia8'],
    include_dirs=[np.get_include()] + get_includes(),
    language='c++',
    extra_compile_args=extra_compile_args
  ),

  Extension(
    'pythiamill.utils.stdetector', ['pythiamill/utils/stdetector.pyx'],
    libraries=['stdc++', 'pythia8'],
    include_dirs=[np.get_include()] + get_includes(),
    language='c++',
    extra_compile_args=extra_compile_args
  )
]

setup(
  name='pythia-mill',

  version='1.0.0',

  description="""Pythia generator for python.""",

  long_description = long_description,

  url='https://github.com/maxim-borisyak/pythia-mill',

  author='Maxim Borisyak',
  author_email='mborisyak at yandex-team dot ru',

  maintainer = 'Maxim Borisyak',
  maintainer_email = 'mborisyak at yandex-team dot ru',

  license='MIT',

  classifiers=[
    'Development Status :: 4 - Beta',

    'Intended Audience :: Science/Research',

    'Topic :: Scientific/Engineering :: Physics',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
  ],

  keywords='Pythia',

  packages=find_packages(exclude=['contrib', 'examples', 'docs', 'tests']),

  extras_require={
    'dev': ['check-manifest'],
    'test': ['nose>=1.3.0'],
  },

  install_requires=[
    'numpy',
    'cython'
  ],

  include_package_data=True,

  package_data = {
  },

  ext_modules = cythonize(extensions, gdb_debug=True),
)