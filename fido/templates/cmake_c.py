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
from fido.core.template import BaseTemplate
import os

class CMakeC(BaseTemplate):
    def get_name(self):
        return "cmake-c"

    def get_description(self):
        return "Create a C project based on CMake."

    def do_build(self):
        if not os.path.isfile("Makefile"):
            os.system( "cmake ." )

        os.system("make")

    def do_clean(self):
        if not os.path.isfile("Makefile"):
            os.system( "cmake ." )

        os.system("make clean")

    def do_reset(self):
        if os.path.isfile("Makefile"):
            os.system("make clean")

        os.system( 'find . -name "CMakeFiles" -or -name "CMakeCache.txt" -or -name "cmake_install.cmake" -or -name "Makefile" | xargs rm -rf' )

def template_load():
    return CMakeC()