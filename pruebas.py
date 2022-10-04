import tweepy

auth = tweepy.OAuthHandler('???',
                           '???')
auth.set_access_token('???',
                      '???')

api = tweepy.API(auth, wait_on_rate_limit=True)

#user = api.get_user("elonmusk")

# Para seguir a gente
#api.create_friendship('elonmusk')
#api.get_friend_ids('0xHispano')
#print(api.get_muted_ids())
#print(api.get_mutes())

user = api.get_user()

print(user.name)
print(user.description)
#for follower in user.followers():
#    print(f'{follower.name} follows {user.name}')

#Returns an array containing the IDs of users being followed by the specified user
    #api.get_friend_ids()
    
#Escribir un tweet
    #api.update_status('mensaje')
    
#Conseguir info de un usuario
    #user = api.get_user('0xHispano')
