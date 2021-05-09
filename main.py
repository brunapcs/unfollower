import tweepy
import os

def get_user_id(screen_name): 
    """
    Args:
        screen_name(str): User's unique "@" name
    
    Returns: 
        id(int): User's unique id
    """

    screen_name = screen_name
    user = api.get_user(screen_name)

    return user.id


if '__name__' == __main__ : 
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_SECRET')


    #init oauth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    my_id = api.me().id

    user_id = get_user_id('brunaparacat')
    followers = api.followers_ids(user_id)

    #save_followers_to_json



