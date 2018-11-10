from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
sid = SentimentIntensityAnalyzer()


def sentiment_analysis(insert_processed_sentence):
    """
    Do the sentiment analysis!!
    """
    sentiment = [0]*len(df["Tweets"])
    for num, player_sent in enumerate(insert_processed_sentence):
        ll = []
        for sentence in player_sent:
            ss = sid.polarity_scores(sentence)
            ll.append(ss)
        sentiment[num] = ll
    return sentiment
    

sentiment_token = sentiment_analysis(sentence_tokenized)
sentiment_token[:2]
sentiment_snowstemmed = sentiment_analysis(sentence_snowstemmeed)
sentiment_snowstemmed[:2]
sentiment_wordnetstemmeed = sentiment_analysis(sentence_wordnetstemmeed)
sentiment_wordnetstemmeed[:2]
