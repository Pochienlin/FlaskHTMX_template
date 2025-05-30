'''
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# USE THIS FILE TO STORE ANY CONSTANTS YOU MAY HAVE FOR THE REST OF YOUR APP
#---- None of the below are actually being used by the service layer currently. They are here as placeholders and examples----
from os import environ, path

var = environ.get('gpt_ep') or 'default'
dir = path.dirname(__file__)
filePath = path.join(dir,'fileName.json')
html_root = path.join(dir,'templates')
src_root = path.join(dir,'assets')
font_root = path.join(dir, 'fonts')