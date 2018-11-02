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
