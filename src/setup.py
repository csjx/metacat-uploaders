#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright 2018 The Regents of the University of California
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Metacat Uploaders

   This library provides classes to upload contents to a Metacat repository via means that are not direct API calls for the content.  It is useful when there are large volumes to register into the server, and where you want to avoid the HTTPS overhead of the web APIs.
"""

import setuptools


def main():
  setuptools.setup(
    name='metacat.uploaders',
    version='1.0.0',
    description='Metacat utilities for batch uploading data',
    author='Christopher Jones',
    author_email='developers@dataone.org',
    url='https://github.com/DataONEorg/d1_python',
    license='Apache License, Version 2.0',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[],
    setup_requires=[
      'setuptools_git >= 1.1'
    ],
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],
    keywords='Metacat batch upload data metadata',
  )


if __name__ == '__main__':
  main()