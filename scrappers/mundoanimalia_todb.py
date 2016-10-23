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

import mysql.connector
from coruna_animal import get_specimen_data



def get_data(con):
    cursor = con.cursor()
    cursor.execute("SELECT id FROM origins WHERE url='http://www.mundoanimalia.com/'")
    origin_id = cursor.fetchone()[0]
    location_id = None
    cursor.close()
    return (origin_id, location_id)

def add_location(cursor, location):
    fields = []
    values = []
    parameters = []

    for i in location:
        if i == 'province':
            try:
                prov_id = int(location[i])
                fields.append('province_id')
                values.append('%s')
                parameters.append(prov_id)
            except ValueError:
                fields.append('province_id')
                values.append('(SELECT id FROM provinces WHERE name LIKE %s)')
                parameters.append(location[i])
        else:
            fields.append(i)
            values.append('%s')
            parameters.append(location[i])

    vquery = ', '.join(values)
    fquery = ', '.join(fields)
    query = 'INSERT INTO locations (%s) VALUES (%s)' % (fquery, vquery)
    cursor.execute(query, parameters)
    cursor.execute("SELECT LAST_INSERT_ID()");
    return cursor.fetchone()[0]

def get_location_id(cursor, locations, url):
    cursor.execute('SELECT id FROM locations WHERE url = %s', [url])
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        location = list(filter(lambda x: x['url']==url, locations.values()))[0]
        return add_location(cursor, location)

def add_to_db(cursor, params, specimen, locations):
    fields = []
    values = []
    parameters = []

    fields += ['origin_id']
    values += ['%s']
    parameters += [params[0]]

    fields.append('origin_identification')
    values.append('%s')
    parameters.append(specimen['origin_internal_id'])

    for i in specimen:
        if i == 'origin_internal_id':
            pass
        elif i == 'race':
            fields.append('race_id')
            values.append('(SELECT id FROM races WHERE name LIKE %s)')
            parameters.append(specimen[i])
        elif i == 'sex':
            if specimen[i] and specimen[i][0] in ('m', 'f'):
                fields.append(i)
                values.append('%s')
                parameters.append(specimen[i][0].upper())
        elif i == 'location_url':
            fields.append('location_id')
            values.append('%s')
            parameters.append(get_location_id(cursor, locations, specimen[i]))
        else:
            fields.append(i)
            values.append('%s')
            parameters.append(specimen[i])

    vquery = ', '.join(values)
    fquery = ', '.join(fields)

    query = 'DELETE FROM specimens WHERE origin_id = %s AND origin_identification = %s'
    cursor.execute(query, [params[0], specimen['origin_internal_id']])

    query = 'INSERT INTO specimens (%s) VALUES (%s)' % (fquery, vquery)
    cursor.execute(query, parameters)
