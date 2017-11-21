#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import os
from credentials import consumer_key, consumer_secret, access_key, access_secret

file_dir = os.path.join(os.path.dirname(__file__))

def get_all_followers(screen_name):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #write the csv
    with open(file_dir + '/export/followersList_@' + screen_name + '.csv', 'wb') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(["id","screen name"])

        for follower in api.followers_ids(screen_name):
            tw_id = api.get_user(follower).id
            tw_sn = api.get_user(follower).screen_name
            #tw_loc = api.get_user(follower).location
            print tw_sn
            tw_export = [tw_id, tw_sn]
            writer.writerow(tw_export)
    print("Export Done !")
    print("Current handle: @" + screen_name)
