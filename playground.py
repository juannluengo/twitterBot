import tweepy


auth = tweepy.OAuthHandler('???',
                           '???')
auth.set_access_token('???',
                      '???')

api = tweepy.API(auth, wait_on_rate_limit=True)

screen_name = 'elonmusk'
user = api.get_user(screen_name)
print(user)
