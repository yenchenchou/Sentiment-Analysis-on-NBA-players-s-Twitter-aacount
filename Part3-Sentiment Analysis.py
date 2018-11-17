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
            ss = analyser.polarity_scores(sentence)
            ll.append(ss)
        sentiment[num] = ll
    return sentiment
    

sentiment_original = sentiment_analysis(df["Tweets"])
sentiment_token = sentiment_analysis(sentence_tokenized)
sentiment_snowstemmed = sentiment_analysis(sentence_snowstemmeed)

# Sentiment Analysis and create dataframe
new_df = pd.DataFrame()
i = 0
for senti_token, snow_stem in zip(sentiment_token, sentiment_snowstemmed):
    #senti_token_pos = [], senti_token_neu = [], senti_token_neg = []
    senti_token_compound = []
    senti_stem_compound = []
    sentiment_result_token = []
    sentiment_result_stem = []

    for s1 in senti_token:
        senti_token_compound.append(s1["compound"])
        if s1["compound"] >= 0.05:
            sentiment_result_token.append("positive")
        elif s1["compound"] <= -0.05:
            sentiment_result_token.append("negative")
        else:
            sentiment_result_token.append("neutral")
            
    for s2 in snow_stem:
        senti_stem_compound.append(s2["compound"])
        if s2["compound"] >= 0.05:
            sentiment_result_stem.append("positive")
        elif s2["compound"] <= -0.05:
            sentiment_result_stem.append("negative")
        else:
            sentiment_result_stem.append("neutral")
        
    tw_df = pd.DataFrame.from_dict({"Tweets":df["Tweets"][i],
                                "Create_time":df["Create_time"][i],
                                "Name":df["Name"][i],
                                "sentiment_token_compound":senti_token_compound,
                                "sentiment_result_token" :sentiment_result_token, 
                                "sentiment_stem_compound":senti_stem_compound,
                                "sentiment_result_stem":sentiment_result_stem})
    new_df = new_df.append(tw_df)
    i += 1
    
  
    Tweets_mix = []
for i, row in enumerate(sentence_snowstemmeed):
    all_row = ""
    for sent in row:
        all_row += sent
    Tweets_mix.append(all_row)

# create the TF-IDF matrix and model first
tfidf_model = TfidfVectorizer(max_df=0.8, max_features=2000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=None, ngram_range=(1,1))

tfidf_matrix = tfidf_model.fit_transform(Tweets_mix) #fit the vectorizer to synopses

print ("In total, there are " + str(tfidf_matrix.shape[0]) + \
      " players and " + str(tfidf_matrix.shape[1]) + " terms.")
