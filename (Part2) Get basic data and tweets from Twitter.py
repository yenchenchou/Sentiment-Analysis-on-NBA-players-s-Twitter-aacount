import tweepy
from tweepy import OAuthHandler
pd.set_option('display.max_columns', None)  # display all columns
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
def tw_from_user(final_tw_account):
    """
    The fuction will get the names, twitter ID, location,
    number of followers, number of friends, and number of
    favourates from the tweepy api. All the data will be 
    put into list format.
    
    Then we perform the inforamtion into a dataframe and 
    return the dataframe.
    """
    names = []
    tw_id = []
    locations = []
    followers_num = []
    friends_num = []
    favourites_num = []
    language = []
    
    for account in final_tw_account:
        results = api.user_timeline(id=account, count = 1)
        for tweet in results:
            names.append(tweet.user.name)
            tw_id.append(tweet.user.screen_name)
            locations.append(tweet.user.location)
            followers_num.append(tweet.user.followers_count) 
            friends_num.append(tweet.user.friends_count)
            favourites_num.append(tweet.user.favourites_count)
            language.append(tweet.user.lang)
    df_basic_info = pd.DataFrame.from_records(
                    zip(names, tw_id, locations, followers_num,
                    friends_num, favourites_num, language),
                    columns = ["Name","Id","Location","Followers",
                               "Friends","Favourites","Language"])
    
    return df_basic_info
  

def get_all_tweet(df_tw1):
    """
    First, we create a space for the whole tweets and 
    the create time of each tweet for each player.
    
    The function is using the tweepy package to get 200
    tweets and the create time of tweet from 30 players
    
    Then we apply the data into a dataframe and return.
    """
    all_nba_tweet = [0]*(len(df_tw1["Id"]))  
    all_creat_time = [0]*(len(df_tw1["Id"]))
    
    for num, ID in enumerate(df_tw1["Id"]):
        tweet_list_byte = []
        tweet_list = []
        creat_time = []
        tweet_content = api.user_timeline(id = ID, count = 200,   tweet_mode = 'extended')
       for twt in tweet_content:
            # if twt.created_at > datetime.datetime(2017, 1, 24, 0, 0, 0):  # extract time after
            tweet_list_byte.append(twt.full_text.encode("utf-8"))
            creat_time.append(twt.created_at)
        for byte_tweet in tweet_list_byte:
            tweet_list.append(byte_tweet.decode("utf-8"))
        all_nba_tweet[num] = tweet_list
        all_creat_time[num] = creat_time
    df_tweet = pd.DataFrame.from_records(zip(all_nba_tweet, all_creat_time),columns = ["Tweets","Create_time"])
    return df_tweet
    
df_tw1 = tw_from_user(final_tw_account)    
df_tweet = get_all_tweet(df_tw1)
df = pd.concat([df_tw1,df_tweet], axis=1)
