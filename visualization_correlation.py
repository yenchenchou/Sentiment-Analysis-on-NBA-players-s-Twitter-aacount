import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

new_df["Date"] = new_df["Create_time"].dt.date
new_df["Date"] = pd.to_datetime(new_df["Date"])
df_for_visual = new_df
del df_for_visual["Create_time"]

# average sentiment score of the players from 2016 to 2018
d1 = df_for_visual.groupby(by = "Name").mean()
d1 = d1.reset_index()
fig, ax = plt.subplots()
ax.set_title('Sentiment of each player overall (token / stemmed)')
sns.set(rc={'figure.figsize':(10,6)})
sns.barplot(x = "sentiment_token_compound", y = "Name",
            alpha = 0.5, data = d1)
sns.barplot(x = "sentiment_stem_compound", y = "Name",
            alpha = 1, data = d1)
            
# monthly sentiment score of each player
d2 = df_for_visual.groupby(by = ["Month","Name"]).mean()
d2 = d2.reset_index()
fig, ax = plt.subplots()
ax.set_title('Sentiment of each player by month')
sns.set(rc={'figure.figsize':(35,25)})
sns.set(font_scale = 1.1)
sns.scatterplot(x = "Month", y = "sentiment_token_compound", 
                hue = "Name", alpha = 0.7, size = "sentiment_token_compound",
                sizes = (10,600), data = d2)
ax.axhline(y = 0.05, color='darkblue', lw=2, linestyle = "--", alpha = 0.5)
ax.axhline(y = -0.05, color='darkblue', lw=2, linestyle = "--", alpha = 0.5)

# Correlation Tests Between Performance & Sentiment
all_player_stats_ls.pop(7)
relation_df = pd.DataFrame()
for i in range(len(df["Name"])):
    tweet_df_tmp = new_df[new_df["Name"] == df["Name"][i]]
    stats_df_tmp = all_player_stats_ls[i]
    df_tmp = pd.merge(tweet_df_tmp, stats_df_tmp, how='inner', on=["Date"])
    relation_df = relation_df.append(df_tmp)
    
# (Pearson’s correlation coefficient, 2-tailed p-value)
stem_cor = pearsonr(relation_df["sentiment_stem_compound"], relation_df["eFG"])
token_cor = pearsonr(relation_df["sentiment_token_compound"], relation_df["eFG"])
print("Pearson in stemmed: {:.3f}, P-value: {:.3f}".format(stem_cor[0],stem_cor[1]))
print("Pearson in token: {:.3f}, P-value: {:.3f}".format(token_cor[0],token_cor[1]))
