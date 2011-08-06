# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import twitter


def twitter_trend(request):

    context = RequestContext(request)
    api = twitter.Api()
    trends = api.GetTrendsCurrent()
    trend_name_list = list()
    for trend in trends:
         trend_name_list.append(trend.name)
    context['trends'] = trend_name_list

    return render_to_response('twitter_trend.html', context)
