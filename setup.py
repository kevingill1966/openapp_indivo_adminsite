from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='openapp_indivo_adminsite',
      version=version,
      description="Admin Site for Indivo",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Framework :: Django",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: POSIX",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        ],
      keywords='indivo',
      author='Kevin Gill (www.OpenApp.ie)',
      author_email='kevin.gill@openapp.ie',
      url='https://github.com/kevingill1966/openapp_indivo_adminsite',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openapp_indivo'],
      include_package_data=True,
      package_data = {'':['README.rst']},
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
