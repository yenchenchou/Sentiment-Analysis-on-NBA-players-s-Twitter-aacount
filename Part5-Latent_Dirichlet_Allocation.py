from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=3, learning_method = 'online')

tfidf_matrix_lda = (tfidf_matrix * 100)
tfidf_matrix_lda = tfidf_matrix_lda.astype(int)
lda.fit(tfidf_matrix_lda)

topic_word = lda.components_
print(topic_word.shape)

n_top_words = 4
topic_keywords_list = []
for i, topic_dist in enumerate(topic_word):
    #Here we select top(n_top_words-1)
    lda_topic_words = np.array(tf_selected_words)[np.argsort(topic_dist)][:-n_top_words:-1] 
    for j in range(len(lda_topic_words)):
        lda_topic_words[j] = vocab_frame_dict[lda_topic_words[j]]
    topic_keywords_list.append(lda_topic_words.tolist())
    
doc_topic = lda.transform(tfidf_matrix_lda)
print (doc_topic.shape)

topic_doc_dict = {}
print ("<Document clustering result by LDA>")
for i in range(len(doc_topic)):
    topicID = doc_topic[i].argmax()
    if topicID not in topic_doc_dict:
        topic_doc_dict[topicID] = [df["Name"][i]]
    else:
        topic_doc_dict[topicID].append(df["Name"][i])
for i in topic_doc_dict:
    print ("Cluster " + str(i) + " words: " + ", ".join(topic_keywords_list[i]))
    print ("Cluster " + str(i) + " Name (" + str(len(topic_doc_dict[i])) + " Players): ")
    print (', '.join(topic_doc_dict[i]), "\n")
