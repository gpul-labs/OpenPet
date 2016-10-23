from twitter import *
import time
import json


#t = Twitter(auth=OAuth(accessToken, accessTokenSecret, consumerKey, consumerToken))
#t.statuses.update(status="OpenPet")

def load_config():
    with open('./config.json') as data_file:
        data = json.load(data_file)
        return {'days':data['delayDays'], 'hours':data['delayHours'], 'minutes':data['delayMinutes'], 'consumerKey':data['consumerKey'], 'consumerToken':data['consumerToken'], 'accessToken':data['accessToken'], 'accessTokenSecret':data['accessTokenSecret']}


def tweet_start():
    cfg = load_config()
    t = Twitter(auth=OAuth(cfg['accessToken'], cfg['accessTokenSecret'], cfg['consumerKey'], cfg['consumerToken']))
    # Calculate the tweet interval in minutes
    tweet_interval = (cfg['days']*24*60 + cfg['hours']*60 + cfg['minutes'])*60
    #while True:
    t.statuses.update(status="Barrrfff")
    #time.sleep(tweet_interval)

tweet_start()
