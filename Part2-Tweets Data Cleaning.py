from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
wordnet = WordNetLemmatizer()
snowballstemmer = SnowballStemmer("english")
stopwords = stopwords.words('english')

def tweets_cleaner(text):

    semiclean_tweet = []
    for tweet in text:
        tweet = re.sub(r'@[A-Za-z0-9]+','',tweet)
        tweet = re.sub(r"http\S+", "", tweet)
        tweet = re.sub(r"#", "", tweet)
        tweet = re.sub(r",", "", tweet)
        tweet = re.sub(r"”", "", tweet)
        tweet = tweet.lower()
        semiclean_tweet.append(tweet)
        
    return semiclean_tweet


def tokenization_and_stem(semiclean_tweet):

    total_token_ls = []
    total_snowballstemmer_token_ls = []
    total_wordNet_token_ls = []
    
    for sentence in semiclean_tweet:
        token_ls = []
        snowballstemmer_token_ls = []
        wordNet_token_ls = []
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            if token not in stopwords:
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
    
    
def back_to_clean_sent(token_ls):
    """
    In order to perform sentiment analysis,
    here we put the words back into sentences. 
    """
    
    clean_sent_ls = []
    for word_ls in token_ls:
        clean_sent = ""
        for word in word_ls:
            clean_sent += (word + " ")
        clean_sent_ls.append(clean_sent)
    return clean_sent_ls


sentence_tokenized = [0]*len(df["Tweets"])
for num, token in enumerate(token_ls):
    sentence_tokenized[num] = back_to_clean_sent(token)
    
sentence_snowstemmeed = [0]*len(df["Tweets"])
for num, token in enumerate(snowstemmer_token_ls):
    sentence_snowstemmeed[num] = back_to_clean_sent(token)
    
sentence_wordnetstemmeed = [0]*len(df["Tweets"])
for num, token in enumerate(wordNet_token_ls):
    sentence_wordnetstemmeed[num] = back_to_clean_sent(token)
view rawback_to_clean_sent.py hosted with ❤ by GitHub
