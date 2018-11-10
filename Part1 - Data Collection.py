import datetime
import json
import numpy as np
import nltk
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

# Get the top 10 players name from ESPN.com
url_player = "http://www.espn.com/nba/story/_/id/24668720/nbarank-2018-19-1-10-best-players-season"
players = requests.get(url_player)
player = BeautifulSoup(players.text, "lxml")

player_list = []
for h2 in player.findAll("h2"):
    for name in h2.findAll({"a":"href"}):
        player_list.append(name.get_text())


# Collect a list of NBA players' Twitter account and their name from reference.com, and match the top 10 players name and their Twitter
url_twitterlink = "https://www.basketball-reference.com/friv/twitter.html"
tweets = requests.get(url_twitterlink)
tweet = BeautifulSoup(tweets.text, "lxml")

player_list2 = []
tw_list = []
for td in tweet.findAll("td",{"data-stat":"player"}):
    for a in td.findAll("a"):
        player_list2.append(a.get_text())
        
for td in tweet.findAll("td",{"data-stat":"twitter_id"}):
    for a in td.findAll("a"):
        tw_list.append(a.get_text())

        
# Scrap the matched players' stats on reference.com
tw_account = {}
final_tw_account = {}
for key, value in zip(player_list2, tw_list):
    tw_account[key] = value

for p, t in tw_account.items():
    if p in player_list:
        final_tw_account[p] = t

        
# Grab the players' tweets and their creation time of each tweet
def get_all_tweet(final_tw_account):

    all_nba_tweet = []
    all_creat_time = []
    followers = []
    friends = []
    favourites = []
    for ID in final_tw_account.values():
        tweet_list = []
        tweet_list_byte = []
        creat_time_list = []
        for twt in tweepy.Cursor(api.user_timeline, id = ID,tweet_mode = 'extended').items(3):
            if twt.created_at > datetime.datetime(2016, 1, 1, 0, 0, 0):  # extract time after
                try:
                    tweet_list.append(twt.retweeted_status.full_text)
                except AttributeError:
                    tweet_list.append(twt.full_text)
                creat_time_list.append(twt.created_at) 

        all_nba_tweet.append(tweet_list)
        all_creat_time.append(creat_time_list)
        followers.append(twt.user.followers_count)
        friends.append(twt.user.friends_count)
        favourites.append(twt.user.favourites_count)
        
    df_tweet = pd.DataFrame.from_records(zip(all_nba_tweet, all_creat_time, followers, friends, favourites),
                                         columns = ["Tweets","Create_time", "Followers", "Friends", "Favourites"])

    return df_tweet


df = get_all_tweet(final_tw_account)

