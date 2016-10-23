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

def clTxt(txt):
    txt = txt.replace('\r','').replace('\n', ' ')
    while '  ' in txt: txt = txt.replace('  ',' ')
    return txt.strip()

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

image_url_base = 'http://www.mundoanimalia.com/'

def get_specimen_data(soup, url):
    data = {}

    cabecera_links = soup.find('div', class_='cabecera').findAll('a')
    species = ''
    if len(cabecera_links) > 1:
        if 'gatos_en_adopcion' in cabecera_links[1]['href']:
            species = 'gat'
        elif 'perros_en_adopcion' in cabecera_links[1]['href']:
            species = 'perr'

    mediaBody = soup.find('div',  class_='media-body')
    data['name'] = mediaBody.find('h1', class_='smalltitle').text.strip()
    data['summary'] = clTxt(mediaBody.find('p').text)

    img_principal = soup.find('img', id='imgprincipal')
    if img_principal:
        data['image'] = img_principal['src']
    else:
        carr = soup.find('div', class_='carousel-inner')
        if carr:
            data['image'] = carr.find('img')['src']
    if 'image' in data and data['image'][0] == '/':
        data['image'] = image_url_base+data['image']

    data['description'] = clTxt(soup.find('div', class_='descipcion_criador_ficha').text)
    
    data['race'] = find_disc_value(species+data['summary'],races)
    data['sex'] = find_disc_value(data['summary'] + data['description'],sexes)

    data['origin_internal_id'] = url.split('/')[-1]
    return data
