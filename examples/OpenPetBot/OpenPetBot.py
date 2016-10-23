from twitter import *
import time

consumerKey='km5gqo5PFFDYjhNJ7leMvR4Fb'
consumerToken='aSjiKbNjl7KyGQxGZ6NV7dHquFFbhgCE9bigfsGfbTjHwoDLJl'
accessToken='17336518-bkJI2BFwWMbna40XXiUgt82IqLIRixMnS7ESybo2D'
accessTokenSecret='kg7cDSu3o7XSXzkQhmTocZze3mlYrWAOwHOryHdjj2rjk'

'''
consumerKey='rC8LlORwWdGgnRfjf8mEm9XfH'
consumerToken='1MwVY67kbx1AyCQMNR3l4mGtDeY9dKkQGfBYbGiDBeFOlxVlHy'
accessToken='790113238671364096-ZCPsH2Am1WQjJUvnPXwBCD564skdsyn'
accessTokenSecret='tkRJzoxQs1Nyuvd5aYXPl1dyLvAD5bJQgbqkxq88HaKZB'
'''
#t = Twitter(auth=OAuth(accessToken, accessTokenSecret, consumerKey, consumerToken))
#t.statuses.update(status="OpenPet")


def tweet_start(days=0, hours=0, minutes=5):
    t = Twitter(auth=OAuth(accessToken, accessTokenSecret, consumerKey, consumerToken))
    # Calculate the tweet interval in minutes
    tweet_interval = (days*24*60 + hours*60 + minutes)*60
    print(tweet_interval)
    while True:
        print('loop')
        # Update the autotweeting parameters
        t.statuses.update(status="Barrrfff")
        time.sleep(tweet_interval)



tweet_start(0,0,1)
