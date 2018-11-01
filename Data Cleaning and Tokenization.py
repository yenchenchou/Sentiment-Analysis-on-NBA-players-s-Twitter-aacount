from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
wordnet = WordNetLemmatizer()
snowballstemmer = SnowballStemmer("english")
stopwords = stopwords.words('english')

def tweets_cleaner(text):
    """
    The function will remove word such as @username,
    the retweet "RT" symbol, url links, and lower the case.
    """
    semiclean_tweet = []
    
    for tweet in text:
        tweet = re.sub(r'RT','',tweet)
        tweet = re.sub(r'@[A-Za-z0-9]+','',tweet)
        tweet = re.sub(r"http\S+", "", tweet)
        tweet = tweet.lower()
        semiclean_tweet.append(tweet)
        
    return semiclean_tweet
    
    
def tokenization_and_stem(semiclean_tweet):
    """
    First,
    This function will parse the string, remove stop words, 
    and remove most of the raw puctuations. Next, it return an 
    array with several elements inside.
    Second,
    There are two advance stemming methods which can extract the
    stem words.They are snowballStemmer and WordNetLemmatizer method.
    """
    total_token_ls = []
    total_snowballstemmer_token_ls = []
    total_wordNet_token_ls = []
    
    for sentence in semiclean_tweet:
        token_ls = []
        snowballstemmer_token_ls = []
        wordNet_token_ls = []
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            if (token not in stopwords) and (re.search('[a-zA-Z]', token)):
                token_ls.append(token)
                snowballstemmer_token_ls.append(snowballstemmer.stem(token))
                wordNet_token_ls.append(wordnet.lemmatize(token))
        total_token_ls.append(token_ls)
        total_snowballstemmer_token_ls.append(snowballstemmer_token_ls)
        total_wordNet_token_ls.append(wordNet_token_ls)
        
    return total_token_ls, total_snowballstemmer_token_ls, total_wordNet_token_ls


df_tweet = [0]*len(df["Tweets"])
token_ls = [0]*len(df["Tweets"])
snowstemmer_token_ls = [0]*len(df["Tweets"])
wordNet_token_ls = [0]*len(df["Tweets"])
for num, text in enumerate(df["Tweets"]):
    token_ls[num], snowstemmer_token_ls[num] , wordNet_token_ls[num] = tokenization_and_stem(tweets_cleaner(text))
