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
from geocoder import osm, google
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from utils import clTxt

phone_url_base = 'http://www.mundoanimalia.com/profesional_protectoras/vercampotelefono/id/%s'
web_url_base = 'http://www.mundoanimalia.com/profesional_protectoras/verweb/id/%s'

pr_data = {'VI': 1,
           'AB': 2,
           'A': 3,
           'AL': 4,
           'AV': 5,
           'BA': 6,
           'PM': 7,
           'Balearic Islands': 7,
           'B': 8,
           'BU': 9,
           'CC': 10,
           'CA': 11,
           'CS': 12,
           'CR': 13,
           'CO': 14,
           'C': 15,
           'CU': 16,
           'GI': 17,
           'GR': 18,
           'GU': 19,
           'SS': 20,
           'H': 21,
           'HU': 22,
           'J': 23,
           'LE': 24,
           'L': 25,
           'LO': 26,
           'LU': 27,
           'M': 28,
           'MA': 29,
           'MU': 30,
           'NA': 31,
           'OR': 32,
           'O': 33,
           'P': 34,
           'GC': 35,
           'PO': 36,
           'SA': 37,
           'TF': 38,
           'S': 39,
           'SG': 40,
           'SE': 41,
           'SO': 42,
           'T': 43,
           'TE': 44,
           'TO': 45,
           'V': 46,
           'VA': 47,
           'BI': 48,
           'ZA': 49,
           'Z': 50,
           'CE': 51,
           'ME': 52 }


def obtain_location_data(soup, url, name):
    data = {}
    data['name'] = name
    id = url.split('/')[-1]

    mediaBody = soup.find('div', class_='media-body')
    address = clTxt(mediaBody.find('p', class_='grey').text).split(': ')[1]
    loc = osm(address)
    if loc.ok:
        data['longitude'] = loc.lng
        data['latitude'] = loc.lat
        if loc.postal:
            data['province'] = int(loc.postal[0:2])
    if not 'province' in data:
        loc = google(address)
        if loc:
            if not 'longitude' in data:
                data['longitude'] = loc.lng
                data['latitude'] = loc.lat
            data['province'] = loc.county
    if data['province'] in pr_data:
        data['province'] = pr_data[data['province']]

    phone_url = phone_url_base % (id,)
    phone_contents = urlopen(phone_url).read().decode()
    phone = clTxt(phone_contents.split('fono: <span>')[1].split('</span>')[0])

    web_url = web_url_base % (id,)
    web_contents = urlopen(web_url).read().decode()
    url = web_contents.split('<iframe')[1].split('src="')[1].split('"')[0]

    data['url'] = url
    data['phone'] = phone
    return data
    

def add_location_data(soup, url, locations):
    mediaBody = soup.find('div',  class_='media-body')

    location_name = clTxt(mediaBody.find('p', class_='clear').text).split(':')[1].strip()
    if not location_name in locations:
        locations[location_name] = obtain_location_data(soup, url, location_name)
    return locations[location_name]['url']
