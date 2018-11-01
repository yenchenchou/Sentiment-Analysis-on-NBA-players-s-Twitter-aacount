import datetime
import json
import numpy as np
import nltk
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
# Extract nba player list and their twitter account from basketball-reference.com
url_twitterlink = "https://www.basketball-reference.com/friv/twitter.html"
tweets = requests.get(url_twitterlink)
tweet = BeautifulSoup(tweets.text, "lxml")
player_list = []
tw_list = []
for td in tweet.findAll("td",{"data-stat":"player"}):
    for a in td.findAll("a"):
        player_list.append(a.get_text())
        
for td in tweet.findAll("td",{"data-stat":"twitter_id"}):
    for a in td.findAll("a"):
        tw_list.append(a.get_text())


# Find the best player on each team according to thesportster.com
url_player = "https://www.thesportster.com/basketball/nba-teams-best-player-officially-ranked/"
players = requests.get(url_player)
player = BeautifulSoup(players.text, "lxml")
player_list2 = []
for h2 in player.findAll("h2",{"class":"item-title"}):
    player_list2.append(h2.get_text())
player_list2[16] = '14 Portland Trail Blazers - Damian Lillard' # type error on the website


# Merge the two data and find the leading players' twitter accout
tw_account = {}
final_tw_account = []
for key, value in zip(player_list, tw_list):
    tw_account[key] = value
for i, j in tw_account.items():
    for x in player_list2:
        if i in x:
            final_tw_account.append(j)
print(len(final_tw_account))
print(final_tw_account[:])  # Damien Lillard ??????
