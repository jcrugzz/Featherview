#What the Trend API Wrapper

import urllib2
import simplejson
from APIs.models import Api

BASE_URL = "http://api.whatthetrend.com/api/v2"


class WhatTheTrend:

    def __init__(self):
        self.trends = []
        self.api_key = Api.objects.get(name="whatTheTrend").key
        self.data = self.__get_trends_json()

    def __parse_trends_with_desc(self):
        for trend in self.data['trends']:
            if trend['description'] != None:
                self.trends.append((trend['name'], trend['description']['text']))
            else:
                self.trends.append((trend['name'], None))

    def __get_trends_json(self):
        url = BASE_URL + "/trends.json?api_key=" + self.api_key
        response = urllib2.urlopen(url).read()
        return simplejson.loads(response)

    def get_trends_with_desc(self):
        self.__parse_trends_with_desc()
        return self.trends

