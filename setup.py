# This file is part of Fido.
#
# Copyright(c) 2015 Simone Margaritelli
# evilsocket@gmail.com
# http://www.evilsocket.net
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 2 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
from setuptools import setup, find_packages
from fido.version import VERSION

import os

def get_data_files():
    data = []
    for folder, subdirs, files in os.walk( 'fido/templates/data/' ):
        for fname in files:
            if fname[0] != '.':
                data.append( os.path.join( folder, fname ) )

    return data

try:
  long_description = open( 'README.md', 'rt' ).read()
except:
  long_description = 'Fido - A minimalistic C/C++ project generator.'

setup( name                 = 'fido',
       version              = VERSION,
       description          = long_description,
       long_description     = long_description,
       author               = 'Simone Margaritelli',
       author_email         = 'evilsocket@gmail.com',
       url                  = 'http://www.github.com/evilsocket/fido',
       packages             = find_packages(),
       include_package_data = True,
       package_data         = { 'fido': get_data_files() },
       scripts              = [ 'bin/fido' ],
       license              = 'GPL',
       zip_safe             = False,
       classifiers          = [
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Unix',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Programming Language :: Python',
            'Topic :: Software Development',
            'Topic :: Software Development :: Build Tools',
            'Topic :: Software Development :: Code Generators',
            'Topic :: Internet',
            'Natural Language :: English'
      ]
)