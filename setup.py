#!/usr/bin/env python
# Copyright (C) 2014 Minted Inc.
# All Rights Reserved

from setuptools import setup

setup(name='sample_service',
  version='0.0.1',
  description='Sample Services - Just a Test',
  author='Chase L',
  author_email='chase@minted.com',
  packages=[
    'sample_service',
  ],
  package_dir={'': 'src'},
  setup_requires=[
    'nose>=1.3.4',
    'm_services'
    ],
  dependency_links = [
    'git+ssh://git@github.com/minted/m_services.git@master#egg=m-services'
    # 'git+ssh://git@github.com:minted/m_services.git@master#egg=m-services'
  ],
  install_requires=[
    'flask==0.10.1',
    'flask-restful==0.2.12',
    'm_services'
  ]
)
