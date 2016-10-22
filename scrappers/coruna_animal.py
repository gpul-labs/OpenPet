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
from datetime import date
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

races = [{'Siam%es': [('gat', 'siam')],
          'Persa': [('gat' ,'pers')],
          'Pastor alem%an': [('pastor', 'aleman')],
          'Can de palleiro': [('palleir',)]},
         {'Gato gen%rico': [('gat',)]},
         {'Perro gen%rico': [('')]}]

def get_race(txt, races):
	query = txt.lower()
	for h in races:
		for i in h:
			for j in h[i]:
				is_races = True
			
				for k in j:
					if k in query:
						is_races = True
					else:
						is_races = False
				
				
				if is_races:
					return i
	return None
	
def txt_to_date(t):
    meses = {'enero': 1,
             'febrero': 2,
             'marzo': 3,
             'abril': 4,
             'mayo': 5,
             'junio': 6,
             'julio': 7,
             'agosto': 8,
             'septiembre': 9,
             'octubre': 10,
             'noviembre': 11,
             'diciembre': 12}
    t = t.split(' ')
    if len(t) != 5:
        return None
    try:
        return date(int(t[4]), meses[t[2]], int(t[0]))
    except ValueError:
        return None
    except IndexError:
        return None

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
    data['race'] = get_race(datosAnimal[1].text + data['summary'],races)
    data['origin_internal_id'] = url.split('/')[-1]
    return data
