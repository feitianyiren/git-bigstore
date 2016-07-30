#!/usr/bin/env python

# Copyright 2015 Lionheart Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

metadata = {}
metadata_file = "bigstore/metadata.py"
exec(compile(open(metadata_file).read(), metadata_file, 'exec'), metadata)

setup(
    name='git-bigstore',
    version=metadata['__version__'],
    license=metadata['__license__'],
    description="Track big files with Git.",
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    url="https://github.com/lionheart/git-bigstore",
    packages=[
        'bigstore.backends',
        'bigstore',
    ],
    scripts=[
        'bin/git-bigstore',
    ],
)

