import tweepy


auth = tweepy.OAuthHandler('SjDFoqWbivn9u2RL6dnfUuqoP',
                           '1U6o8Oy0DBtSQeC9H025LIyIbl3Z8mujn1sks8KBxTXte6i8UD')
auth.set_access_token('1529083290103304192-oduTF9v0QORyzKBllWdLevGcyRN3UM',
                      'GUdStjYP0YQgpbYzwkyNXLFCSwjvfH9z52lJgw5Wn3K9P')

api = tweepy.API(auth, wait_on_rate_limit=True)

screen_name = 'elonmusk'
user = api.get_user(screen_name)
print(user)