import tweepy

auth = tweepy.OAuthHandler('VZZxQzssNv6fTRWH26xNAAodi',
                           'cutVY6mQ8Yf1c0uk63XgtzRgo9qjGTfUKTYJ6NIlih8QQLR1RZ')
auth.set_access_token('1529083290103304192-9wniswQWeftUVpfQf3wCgHu2ZAZ2GY',
                      'r5HGlfKDR96qLFirpl34wGv2M2dgKVi962c9dOgG8WA5p')

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