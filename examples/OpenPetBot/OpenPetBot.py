#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from twitter import *
import time, json, requests, random

def load_config():
    with open('./config.json') as data_file:
        data = json.load(data_file)
        return {'days':data['delayDays'], 'hours':data['delayHours'], 'minutes':data['delayMinutes'], 'consumerKey':data['consumerKey'], 'consumerToken':data['consumerToken'], 'accessToken':data['accessToken'], 'accessTokenSecret':data['accessTokenSecret'], 'apiUrl':data['apiUrl'], 'recordsPerRequest':data['recordsPerRequest']}

def tweet_start():
    cfg = load_config()
    t = Twitter(auth=OAuth(cfg['accessToken'], cfg['accessTokenSecret'], cfg['consumerKey'], cfg['consumerToken']))

    t_up = Twitter(domain='upload.twitter.com/',
                  api_version='1.1',
                  auth=OAuth(cfg['accessToken'], cfg['accessTokenSecret'], cfg['consumerKey'], cfg['consumerToken']))

    # tweet_interval = (cfg['days']*24*60 + cfg['hours']*60 + cfg['minutes'])*60

    # recoger los datos de los animaeles
    url = cfg['apiUrl']+'?last='+cfg['recordsPerRequest']
    response = requests.get(url).json()
    # elijo uno al azar
    randId = response[random.randrange(0,len(response))]['id']
    url = cfg['apiUrl']+'/'+str(randId)
    response = requests.get(url).json()
    # obtengo imagen
    imagedata = requests.get(response['image'], stream=True).content
    #compongo texto
    msg = str("Saluda a "+response['name']+" este "+response['specie']['name']+' busca un hogar, conocelo en '+response['location']['name']+" "+response['location']['url']+".")
    #subo la imagen
    id_img = t_up.media.upload(media=imagedata)["media_id_string"]

    t.statuses.update(status= msg,media_ids=id_img)

tweet_start()
