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

    return render_to_response('index.html', context, c)

@csrf_exempt
def twitter_trend(request):

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
            photo_url = shorturl.url(photo_id)
            photo_list.append(photo_url)
            if count == 2:
                break

        
        if count != 0 :
            photos_for_trends[trend_name] = photo_list

    html_output_array = list()
    response = HttpResponse()
    for name, url_array in photos_for_trends.iteritems():
        for url in url_array:
            value = "<div class='masonry-brick'><img class='" + name + "' src='" + url + "'/></div>"
            response.write(value)
    
    return response

