from sklearn.cluster import KMeans
num_clusters = 3
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

# create DataFrame films from all of the input files.
films = {'Name': df["Name"].tolist(), 'Cluster': clusters}
frame = pd.DataFrame(films, index = [clusters])
frame

l1, l2 = "", ""
for player in sentence_tokenized:
    for sent in player:
        l1 += sent
docs_tokenized = l1.split()

for player in sentence_snowstemmeed:
    for sent in player:
        l2 += sent
docs_snowstemmed = l2.split()

vocab_frame_dict = {docs_snowstemmed[x]:docs_tokenized[x] for x in range(len(docs_snowstemmed))}
tf_selected_words = tfidf_model.get_feature_names()

print ("Clustering result by K-means")
# km.cluster_centers_ denotes the importances of each items in centroid.
# We need to sort it in decreasing-order and get the top k items.
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

Cluster_keywords_summary = {}
for i in range(num_clusters):
    print ("Cluster " + str(i) + " words: ", end='')
    Cluster_keywords_summary[i] = []
    for ind in order_centroids[i, :3]: #replace 5 with n words per cluster
        Cluster_keywords_summary[i].append(vocab_frame_dict[tf_selected_words[ind]])
        print (vocab_frame_dict[tf_selected_words[ind]] + ",", end='')

    cluster_NBA = frame.loc[i]['Name'].values
    print("\n", ", ".join(cluster_NBA), "\n")
