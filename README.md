# Sentiment Analysis on NBA leading players' Twitter Accounts 
It is known that the leading players in a team play a vital role in the game-winning. Hence, we are curious if the players’ emotion before the game will have correlation on their performance or even on the game result. To measure this effect, we choose Twitter as our tool to measure the players’ sentiment because a majority of NBA players tweet their opinions or mind on twitter.

However, it is time-consuming to evaluate each player’s tweet in the league; hence we will be just focusing on the top 10 players according to ESPN.com. Now someone may start to debate why those are the best players on each team but here we just use one of the examples website instead of any personal preferences.

In the analysis, I will be using Python as the programming language and this topic will involve technics such as web scraping, clustering, data visualization, and natural language processing.


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
import matplotlib.pyplot as plt
import numpy as np
import nltk
import pandas as pd
import requests
import re
import tweepy
import seaborn as sns
from bs4 import BeautifulSoup
from tweepy import OAuthHandler
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.sentiment.util import *
from nltk import tokenize
from scipy.stats import pearsonr
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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
We will implement the sentiment analysis to the original tweets, sentence_tokenized, and sentence_snowstemmeed to observe the difference between these methods and check their effect. When talking about sentiment analysis, there are three common types we use and rule-based method will be selected in this chapter because it is easier to apply and there is no need to have an actual training set to train the data.

* Rule-based: Perform sentiment analysis based on a set of predefined rules and sentiment score.
* Automatic: Using machine learning techniques to learn from data.
* Hybrid: Combine both rule-based and automatic methods.

### Part4 "K-means Clustering"
Before begin the clustering, we must create the TF-IDF matrix and model first. TF-IDF refers to Term Frequency–Inverse Document Frequency and it is a product of two statistics that reflect how important a word is to a document in a collection or corpus:

* Term frequency: The weight of a term that occurs in a document is simply proportional to the term frequency.
* Inverse document frequency: The specificity of a term can be quantified as an inverse function of the number of documents in which it occurs.
In order to make things simple, here we only use the stemmed sentence and product the TF-IDF matrix. The Tweets_mix is just a list that gathering all the stemmed sentences and only doing so will we able to generate the TF-IDF matrix.

### Part5 "Latent Dirichlet Allocation"
In this article, we set 3 components since we also have 3 clusters in K-means methods. The n_stop_words means that we are hoping to see the first 3 frequent words in each topic. The number is set to 4 is because of the indexing issue so we have to +1 for the result of 3.

### Part6 "Data Visualization and Correlation Test"
we are finally going to see whether there is any statistical correlation between the players' performance on the court with their tweets. However, is our article it points out that there is no any correlation between them under the Pearson correlation test.

