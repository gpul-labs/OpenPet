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

from datetime import date

def find_disc_value(txt, options):
    query = txt.lower()
    for h in options:
        for i in h:
            for j in h[i]:
                found_option = True
                for k in j:
                    if not k in query:
                        found_option = False
                if found_option:
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
