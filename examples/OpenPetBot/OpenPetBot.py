from twitter import *
import time
import json
import requests
import random

#t = Twitter(auth=OAuth(accessToken, accessTokenSecret, consumerKey, consumerToken))
#t.statuses.update(status="OpenPet")

def load_config():
    with open('./config.json') as data_file:
        data = json.load(data_file)
        return {'days':data['delayDays'], 'hours':data['delayHours'], 'minutes':data['delayMinutes'], 'consumerKey':data['consumerKey'], 'consumerToken':data['consumerToken'], 'accessToken':data['accessToken'], 'accessTokenSecret':data['accessTokenSecret'], 'apiUrl':data['apiUrl'], 'recordsPerRequest':data['recordsPerRequest']}


def tweet_start():
    cfg = load_config()
    t = Twitter(auth=OAuth(cfg['accessToken'], cfg['accessTokenSecret'], cfg['consumerKey'], cfg['consumerToken']))
    # Calculate the tweet interval in minutes
    tweet_interval = (cfg['days']*24*60 + cfg['hours']*60 + cfg['minutes'])*60

    # recoger los datos
    url = cfg['apiUrl']+'?last='+cfg['recordsPerRequest']
    response = requests.get(url).json()

    randId = response[random.randrange(0,len(response))]['id']

    url = cfg['apiUrl']+'/'+str(randId)
    response = requests.get(url).json()
    while True:
        t.statuses.update(status="Saluda a "+response['name']+" este "+response['specie']['name']+' busca un hogar, si estas interesado ponte en contacto con '+response['location']['name']+"("+response['location']['url']+")."+response['image'])
        time.sleep(tweet_interval)

tweet_start()
