# Create your views here.
from django.shortcuts import render_to_response
from django.http import *
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.decorators.csrf import requires_csrf_token
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson
import tweepy
from utils import *
import pdb

CALLBACK_URL = "http://localhost:8000/callback/"


@requires_csrf_token
def index(request):

    context = RequestContext(request)
    if check_key(request):
        return HttpResponseRedirect(reverse('info'))
    else:
        context["photos_for_trends"] = twitter_trend()
        return render_to_response('index.html', context)


@requires_csrf_token
def main(request):
    """
    main view of app, either login page or info page
    """
    context = RequestContext(request)
    # if we haven't authorised yet, direct to login page
    if check_key(request):
        return HttpResponseRedirect(reverse('info'))
    else:
        return render_to_response('login.html', context)


def unauth(request):
    """
    logout and remove all session data
    """
    if check_key(request):
        api = get_twitter_api(request)
        request.session.clear()
        logout(request)
    return HttpResponseRedirect(reverse('main'))


def info(request):
    """
    display some user info to show we have authenticated successfully
    """
    if check_key(request):
        context = RequestContext(request)
        api = get_twitter_api(request)
        user = api.me()
        context['user'] = user
        return render_to_response('info.html', context)
    else:
        return HttpResponseRedirect(reverse('main'))


@requires_csrf_token
def auth(request):
    # start the OAuth process, set up a handler with our details
    #pdb.set_trace()
    twitter_oauth = Api.objects.get(name="twitter_oauth")
    key = str(twitter_oauth.key)
    secret = str(twitter_oauth.secret)
    #pdb.set_trace()
    oauth = tweepy.OAuthHandler(key, secret, CALLBACK_URL)
    # direct the user to the authentication url
    auth_url = oauth.get_authorization_url()
    response = HttpResponseRedirect(auth_url)
    # store the request token
    request.session['unauthed_token_tw'] = (oauth.request_token.key, oauth.request_token.secret)
    return response


def callback(request):
    verifier = request.GET.get('oauth_verifier')
    twitter_oauth = Api.objects.get(name="twitter_oauth")
    key = twitter_oauth.key
    secret = twitter_oauth.secret
    oauth = tweepy.OAuthHandler(key, secret)
    token = request.session.get('unauthed_token_tw', None)
    # remove the request token now we don't need it
    request.session.delete('unauthed_token_tw')
    oauth.set_request_token(token[0], token[1])
    # get the access token and store
    try:
        oauth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error, failed to get access token'
    request.session['access_key_tw'] = oauth.access_token.key
    request.session['access_secret_tw'] = oauth.access_token.secret
    response = HttpResponseRedirect(reverse('info'))
    return response


def twitter_trend():

    twitter = tweepy.API()
    # Location set to 1 for World Trends (Location independent)
    data = twitter.trends_location(1)

    flickr = get_flickr_api()
    photos_for_trends = dict()
    for trend in data[0]["trends"]:
        trend_name = trend["name"]

        if '#' in trend_name:
            trend_name = trend_name.lstrip('#')
        photo_list = list()
        count = 0
        for photo in flickr.walk(text=trend_name, safe_search=1,
                                            content_type=7, per_page=2):
            count += 1
            photo_id = photo.get('id')
            farm_id = photo.get('farm')
            server_id = photo.get('server')
            secret = photo.get('secret')
            photo_url = \
                "http://farm" + farm_id + ".static.flickr.com/" + server_id + "/" + \
                    photo_id + "_" + secret + "_z.jpg"
            photo_list.append(photo_url)
            if count == 2:
                break

        if count != 0:
            photos_for_trends[trend_name] = photo_list

    return photos_for_trends


def check_key(request):
    """
    Check to see if we already have an access_key stored, if we do then we have already gone through
    OAuth. If not then we haven't and we probably need to.
    """
    try:
        access_key = request.session.get('access_key_tw', None)
        if not access_key:
            return False
    except KeyError:
        return False
    return True
