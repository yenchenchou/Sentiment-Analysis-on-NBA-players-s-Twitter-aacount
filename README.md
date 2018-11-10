# Sentiment Analysis on NBA leading players' Twitter Accounts 
It is known that the leading players in a team play a vital role in the game-winning. Hence, we are curious if the players' emotion before the game will have correlation on their performance or even on the game result. To measure this effect, we choose Twitter as our tool to measure the players' sentiment because a majority of NBA players tweet their opinions or mind on twitter.
However, it is time-consuming to evaluate each player's tweet in the league; hence we will be just focusing on the top 10 players according to ESPN.com. Now someone may start to debate why those are the best players on each team but here we just use one of the examples website instead of any personal preferences.


*See more details on my [blog](https://medium.com/@intelchou/do-tweets-from-nba-leading-players-have-correlations-with-their-performance-7358c79aa216)*

## Metrics
Since the ultimate goal is to measure the correlation between sentiment and game performance. The sentiment here is by calculating the positive or negative score based on polarity and valence. We will discuss this later.
As for the performance, we use Efficient Field Goals(eFG) in this article due to its good balance between simplicity and accuracy.
eFG formula: (FG + 0.5 * 3P) / FGA

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
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
from tweepy import OAuthHandler
```

## Processing Steps
In the analysis, I will be using Python as the programming language and this topic will involve technics such as web scraping, clustering, data visualization, and natural language processing.

### Part1 "Scraping Twitter Account from Web and Twitter"
* Get the top 10 players name from ESPN.com
* Collect a list of NBA players' Twitter account and their name from reference.com, and match the top 10 players name and their Twitter
* Scrap the matched players' stats on reference.com
* Grab the players' tweets and their creation time of each tweet.

### Part2 "Tweets Data Cleaning and Tokenization"
In this section, we are going to clean the tweets since it contains unnecessary texts and implement three different tokenozing methods. 
The unnecessary texts include:
* @’mention: Remove the “@username”(screen name in twitter) no matter it is from retweet or original tweet
* URL: Remove all possible URL links since we are not going to dive deeper into the links
* stopwords: Remove common words that do not have much meaning
* special characters: Even though sometimes special characters have some special meanings, considering the simplicity of the process, we will remove in the research
* hash(#): We believe that using hashtags is also a symbol showing stronger emotion on tweets so here we only take out the “#” symbol from the hashtags.

### Part3 "Sentiment Analysis"
Now, finally we are ready for the analysis and let us recap some important things we have made:

1. token_ls: word lists that are tokenized
2. snowstemmer_token_ls: word lists that are tokenized and stemmed in snowball method
3. wordNet_token_ls: word lists that are tokenized and stemmed in wordnet method
4. sentence_tokenized: put the tokens in “token_ls” back into sentence structure
5. sentence_snowstemmeed: put the tokens in “snowstemmer_token_ls” back into sentence structure
6. sentence_wordnetstemmeed: put the tokens in “wordNet_token_ls” back into sentence structure. The SentimentIntensityAnalyzer() will generate four metrics including positive score, neutral score, negative score, and compound score.
