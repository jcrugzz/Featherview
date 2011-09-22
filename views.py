# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson
import twitter
from flickrapi import shorturl, FlickrAPI

api_key = '133d83e98d25f8bc60b9aa7dbbe4d61e'

@requires_csrf_token
def index(request):
    c ={}
    context = RequestContext(request) 
    context["photos_for_trends"] = twitter_trend()

    return render_to_response('index.html', context, c)

def twitter_trend():

    api = twitter.Api()
    trends = api.GetTrendsCurrent()

    flickr = FlickrAPI(api_key)
    photos_for_trends = dict()
    for trend in trends:
        trend_name = trend.name
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
                "http://farm" +  farm_id + ".static.flickr.com/" + server_id + "/" + \
                    photo_id + "_" + secret +"_z.jpg"
            photo_list.append(photo_url)
            if count == 2:
                break

        
        if count != 0 :
            photos_for_trends[trend_name] = photo_list

    return photos_for_trends 

