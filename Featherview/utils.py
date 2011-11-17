import tweepy
from APIs.models import Api
from flickrapi import FlickrAPI


def get_twitter_api(request):
    # set up and return a twitter api object
    twitter_oauth = Api.objects.get(name="twitter_oauth")
    key = twitter_oauth.key
    secret = twitter_oauth.secret
    oauth = tweepy.OAuthHandler(key, secret)
    access_key = request.session['access_key_tw']
    access_secret = request.session['access_secret_tw']
    oauth.set_access_token(access_key, access_secret)
    api = tweepy.API(oauth)
    return api


def get_flickr_api():
    flickr_api = Api.objects.get(name='flickr')
    api_key = flickr_api.key

    flickr = FlickrAPI(api_key)
    return flickr
