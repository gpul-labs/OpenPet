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
import re
import math


try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

base_url = 'http://www.coruna.es/adopcion/gl/animais'
page_query = '?argPag='

def get_specimen_links():
    ret = []
    # 1ª llamada a la pagina
    main_page_bs = BeautifulSoup(urlopen(base_url).read(), 'html.parser')
    # obtengo el # de resultados
    _resultados_sitio = re.findall('\d+',str(main_page_bs.find('p', class_='resultadosBot')))[0]
    # obtengo el # de resultados por pagina
    _resultados_pagina = re.findall('\d+',str(main_page_bs.find('li', class_='numPags')))[0]
    # deduzco el numero de paginas
    _paginas = int(math.ceil(float(_resultados_sitio) / float(_resultados_pagina))+1)
    # ya que he cargado la 1ª pagina saco todos los enlaces
    for specimen in main_page_bs.findAll('li', class_='listadoContenido'):
        ret.append(specimen.find('a')['href'])
    # si hay mas de una pagina continuo
    if(_paginas>1):
        for pagina in range(2,_paginas):
            uri = str(base_url)+str(page_query)+str(pagina)
            main_page_bs = BeautifulSoup(urlopen(uri).read(), 'html.parser')
            for specimen in main_page_bs.findAll('li', class_='listadoContenido'):
                ret.append(specimen.find('a')['href'])
    return ret

#print ('\n'.join(get_specimen_links()))
