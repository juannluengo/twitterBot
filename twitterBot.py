import tweepy
import time

auth = tweepy.OAuthHandler('???',
                           '???')
auth.set_access_token('???',
                      '???')

api = tweepy.API(auth, wait_on_rate_limit=True)

#user = api.me()

search = 'Solana'
nrTweets = 500

api.get_followers()

#Start liking tweets from people usinf the word "search"
#Problem: isn't organic enough, as most of the content I like comes from bots
#Possible solution: give likes to followers from existing accounts
for tweet in tweepy.Cursor(api.search_tweets, search, count=100).items(nrTweets):
    try:
        tweet.favorite()
        print('Tweet Liked')
        time.sleep(10) 
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break

user = api.get_user()
print(user)
#Get list of followers from someone
ids = []
for page in tweepy.Cursor(api.get_follower_ids(), screen_name="McDonalds").pages():
    ids.extend(page)
    time.sleep(60)

api.get_follower_ids()
