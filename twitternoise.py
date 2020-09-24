# Twitter Noise
# 2020-09-23

# Load tweet data set
#   http://help.sentiment140.com/for-students/
#   The data is a CSV with emoticons removed. Data file format has 6 fields:
#       0 - the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
#       1 - the id of the tweet (2087)
#       2 - the date of the tweet (Sat May 16 23:58:44 UTC 2009)
#       3 - the query (lyx). If there is no query, then this value is NO_QUERY.
#       4 - the user that tweeted (robotickilldozr)
#       5 - the text of the tweet (Lyx is cool)
# Start loop
#   Select Tweet
#   Publish

import csv, random

TWEET_FILENAME = 'data\\training.1600000.processed.noemoticon.csv'
NUM_TWEETS_OUT = 100

tweet_data = []


print('Loading tweets...')
with open(TWEET_FILENAME) as dataset_file:
    csv_reader = csv.reader(dataset_file)
    for row in csv_reader:
        tweet_data.append(row)
    print('Loaded', len(tweet_data), 'tweets.')

for i in range(NUM_TWEETS_OUT):
    random_index = random.randrange(len(tweet_data))
    random_tweet = tweet_data[random_index]
    # print(random_tweet)
    print(random_index, ':', random_tweet[4], ':', random_tweet[5])

print('\nFinished')