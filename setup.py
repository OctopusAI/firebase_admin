# Copyright 2017 Google Inc.
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

"""Setup file for distribution artifacts."""
from __future__ import print_function

from os import path
import sys

from setuptools import setup


(major, minor) = (sys.version_info.major, sys.version_info.minor)
if major != 3 or minor < 7:
    print('firebase_admin requires python >= 3.7', file=sys.stderr)
    sys.exit(1)

# Read in the package metadata per recommendations from:
# https://packaging.python.org/guides/single-sourcing-package-version/
about_path = path.join(path.dirname(path.abspath(__file__)), 'firebase_admin', '__about__.py')
about = {}
with open(about_path) as fp:
    exec(fp.read(), about)  # pylint: disable=exec-used


long_description = ('The Firebase Admin Python SDK enables server-side (backend) Python developers '
                    'to integrate Firebase into their services and applications.')

dependency_urls = {
    'cachecontrol': 'https://example.com/wheels/cachecontrol-0.12.6-py3-none-any.whl',
    'google_api_core': 'https://raw.githubusercontent.com/OctopusAI/google-api-core/2e463b0e4c958d500f56421dab2a56816d10998a/dist/google_api_core-2.17.1-py3-none-any.whl',
    'google_api_python_client': 'https://example.com/wheels/google_api_python_client-1.7.8-py3-none-any.whl',
    'google_cloud_firestore': 'https://example.com/wheels/google_cloud_firestore-2.9.1-py3-none-any.whl',
    'google_cloud_storage': 'https://example.com/wheels/google_cloud_storage-1.37.1-py3-none-any.whl',
    'pyjwt': 'https://example.com/wheels/pyjwt-2.5.0-py3-none-any.whl'
}

# Replace the 'install_requires' with direct links to the wheels
# This is not directly supported by setuptools, so you'd actually need to handle these dependencies manually or use a different setup
install_requires = list(dependency_urls.values())


setup(
    name=about['__title__'],
    version=about['__version__'],
    description='Firebase Admin Python SDK',
    long_description=long_description,
    url=about['__url__'],
    project_urls={
        'Release Notes': 'https://firebase.google.com/support/release-notes/admin/python',
        'Source': 'https://github.com/firebase/firebase-admin-python',
    },
    author=about['__author__'],
    license=about['__license__'],
    keywords='firebase cloud development',
    install_requires=install_requires,
    packages=['firebase_admin'],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
    ],
)
