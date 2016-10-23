#!/usr/bin/env python
#encoding: utf-8

#Copyright (C) 2016 José Millán Soto <fid@gpul.org>
#Copyright (C) 2016 Miguel López Cuesta <lopezcuestam@gmail.com>
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
from utils import find_disc_value, txt_to_date

races = [{'Siam%es': [('gat', 'siam')],
          'Persa': [('gat' ,'pers')],
          'Pastor alem%an': [('pastor', 'aleman')],
          'Pastor belga': [('pastor', 'belga')],
          'Pit bull': [('pit', 'bul')],
          'American Staffordshire terrier': [('amstaff',), ('american','ford')],
          'Can de palleiro': [('palleir',)]},
         {'Pastor': [('pastor',)]},
         {'Gato gen%rico': [('gat',)]},
         {'Perro gen%rico': [('',)]}]

sexes = [{'male': [('gato ',), ('perro ',), ('macho',), ('cachorro',)],
          'female': [('gata ',), ('perra ',), ('hembra',), ('cachorra',)]}]

base_img_domain = 'http://www.coruna.es/'

def get_specimen_data(url):
    main_page_contents = urlopen(url).read()
    soup = BeautifulSoup(main_page_contents, 'html.parser')
    data = {}
    detalleAnimal = soup.find('div', id='detalleAnimal')
    data['name'] = detalleAnimal.find('h2').text.strip()
    data['image'] = base_img_domain + detalleAnimal.find('img')['src']
    datosAnimal = detalleAnimal.find('dl').findAll('dd')
    data['birthdate'] = txt_to_date(datosAnimal[0].text)
    data['entrydate'] = txt_to_date(datosAnimal[2].text)
    data['summary'] = datosAnimal[3].text
    data['description'] = datosAnimal[4].text
    data['race'] = find_disc_value(datosAnimal[1].text + data['summary'],races)
    data['sex'] = find_disc_value(datosAnimal[1].text + data['summary'] + data['description'],sexes)
    data['origin_internal_id'] = url.split('/')[-1]
    return data
