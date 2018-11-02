# Sentiment Analysis on NBA leading players' Twitter Accounts 
It is known that the leading players in a team play a vital role in the game-winning. Hence, we are curious if the players’ emotion before the game will affect their performance or even have an impact on the game result. To measure this effect, we choose Twitter as our tool to measure the players’ sentiment because a majority of NBA players tweet their opinions or mind on twitter. However, it is time-consuming to evaluate each player’s tweet in the league; hence we will be just focusing on the leading players. The leading players here we define are players who have the most followers in each team, which means there will be a total of 30 players in our analysis.

## Prerequisites
Before we start, these packages are required for our analysis:
```Python
import datetime
import json
import numpy as np
import nltk
import pandas as pd
import requests
import re
import tweepy
from bs4 import BeautifulSoup
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
from tweepy import OAuthHandler
```

## Processing Steps
In the analysis, I will be using Python as the programming language and this topic will involve technics such as web scraping, and some simple natural language processing. The code is seperated in five parts and the main function of each part will be shown through the topics. More details will be illustrated in the functions.

### Part1 "Scraping Twitter Account from Web"
the first step to collect Twitter account from NBA players, we need to find a place it provides all of their twitter accounts. Also, we need a blog or website that defines the best player on each team. Luckily, I found the resource after a couple of minutes: basketball-reference.com and thesportster.com. Now someone may start to debate why those are the best players on each team but here we just use one of the examples website instead of any personal preferences.

Here I implement requests and BeautifulSoup package from Python to extract the all NBA players’ name and their corresponding Twitter ID. The extracted data will be put into lists temporarily.

### Part2 "Get basic data and tweets from the Twitter accounts"
Now, here Twitter comes, we start to grab the tweet data according to the accounts we just got. But before things start, remember you should already have a Twitter developer account or you cannot proceed with the process.

Note that the consumer_key, consumer_secret, access_token, and access_secret should be using your own token. Do not share with anyone!!

### Part3 "Data Cleaning and Tokenization"
In this section, we are going to clean the tweets since it contains unnecessary texts and implement three different tokenozing methods. 
The unnecessary texts include:
* @’mention: Remove the “@username”(screen name in twitter) no matter it is from retweet or original tweet
* URL: Remove all possible URL links since we are not going to dive deeper into the links
* stopwords: Remove common words that do not have much meaning
* special characters: Even though sometimes special characters have some special meanings, considering the simplicity of the process, we will remove in the research
* hash(#): We believe that using hashtags is also a symbol showing stronger emotion on tweets so here we only take out the “#” symbol from the hashtags.

### Part4 "Put tokens back into to sentence structure (cleaned sentence!)"
Here we put the tokens back to sentence structures.

### Part5 "Sentiment Analysis"
Now, finally we are ready for the analysis and let us recap some important things we have made:

1. token_ls: word lists that are tokenized
2. snowstemmer_token_ls: word lists that are tokenized and stemmed in snowball method
3. wordNet_token_ls: word lists that are tokenized and stemmed in wordnet method
4. sentence_tokenized: put the tokens in “token_ls” back into sentence structure
5. sentence_snowstemmeed: put the tokens in “snowstemmer_token_ls” back into sentence structure
6. sentence_wordnetstemmeed: put the tokens in “wordNet_token_ls” back into sentence structure. The SentimentIntensityAnalyzer() will generate four metrics including positive score, neutral score, negative score, and compound score.

*Later on, we will be demonstrating some exploring data analysis, clustering, and see the correlations between the players’ performance and their sentiment on Twitter.*
