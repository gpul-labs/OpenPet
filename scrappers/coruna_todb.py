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
    cursor.execute("SELECT id FROM origins WHERE url='http://www.coruna.es/adopcion'")
    origin_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM locations WHERE url='http://www.coruna.es/adopcion'")
    location_id = cursor.fetchone()[0]
    cursor.close()
    return (origin_id, location_id)

def add_to_db(cursor, params, specimen):
    fields = []
    values = []
    parameters = []

    fields += ['origin_id', 'location_id']
    values += ['%s', '%s']
    parameters += list(params)

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
                parameters.append(specimen[i][0])
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
