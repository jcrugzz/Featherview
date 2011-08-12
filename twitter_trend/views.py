# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import twitter
from flickrapi import shorturl, FlickrAPI

api_key = '133d83e98d25f8bc60b9aa7dbbe4d61e'

def twitter_trend(request):

    context = RequestContext(request)
    api = twitter.Api()
    trends = api.GetTrendsCurrent()

    flickr = FlickrAPI(api_key)
    photos_for_trends = dict()
    for trend in trends:
        trend_name = trend.name
        if '#' in trend_name:
            trend_name = trend_name.lstrip('#')
        photo_dict = dict()
        count = 0
        for photo in flickr.walk(text=trend_name, safe_search=1,
                                            content_type=7, per_page=2):
            count += 1
            photo_id = photo.get('id')
            photo_url = shorturl.url(photo_id)
            photo_dict[photo_id] = photo_url
            if count == 2:
                break

        
        if count != 0 :
            photos_for_trends[trend_name] = photo_dict


    context['photos'] = photos_for_trends

    return render_to_response('twitter_trend.html', context)
