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
from mundoanimalia_animal import get_specimen_data

base_domain = 'http://www.mundoanimalia.com'
page_path = '/animales_en_adopcion/protectora/pagina/%s' #%s is the page number

def get_specimen_links(page_num = 1, cont_pages = 10):
    ret = []

    def_uri = (base_domain+page_path) % (page_num,)
    soup = BeautifulSoup(urlopen(def_uri).read(), 'html.parser')
    thumbs = soup.findAll('div', class_='thumb')
    for thumb in thumbs:
        ret.append(thumb.find('a')['href'])

    if (cont_pages):
        ret += get_specimen_links(page_num + 1, cont_pages - 1)

    return ret

def get_specimen_dict(page_num = 1, cont_pages = 10):
    links = get_specimen_links(page_num, cont_pages)
    res = {}
    for i in links:
        page_contents = urlopen(i).read()
        soup = BeautifulSoup(page_contents, 'html.parser')
        data = get_specimen_data(soup, i)
        res[data['origin_internal_id']] = data
    return res

from db import get_connection
from mundoanimalia_todb import get_data, add_to_db

connection = get_connection()

parameters = get_data(connection)

cursor = connection.cursor()
for animal in get_specimen_dict().values():
    add_to_db(cursor, parameters, animal)

cursor.close()
connection.commit()
connection.close()

