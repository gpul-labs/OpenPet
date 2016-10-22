#!/usr/bin/env python
#encoding: utf-8

#Copyright (C) 2016 José Millán Soto <fid@gpul.org>
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software Foundation,
#Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

base_url = 'http://www.coruna.es/adopcion/gl/animais'

main_page_contents = urlopen(base_url).read()

main_page_bs = BeautifulSoup(main_page_contents, 'html.parser')

def get_specimen_links(soup):
    ret = []
    for specimen in soup.findAll('li', class_='listadoContenido'):
        ret.append(specimen.find('a')['href'])
    return ret

print ('\n'.join(get_specimen_links(main_page_bs)))
