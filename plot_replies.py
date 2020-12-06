import pandas as pd;
import matplotlib.pyplot as plt;\

# read your reply data into pandas dataframe
df = pd.read_csv('data.csv') 

# get the names of all the replies
reply_gang = df['Screen name']

# plot the names that appear the most often
plt.rcParams["figure.figsize"] = (10,5)
reply_gang.value_counts()[:15].sort_values().plot(kind = 'barh');

# show the plots
plt.title('# replies');
plt.savefig('replies.png')
plt.show()
