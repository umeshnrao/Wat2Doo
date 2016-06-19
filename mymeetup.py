from __future__ import unicode_literals

import requests
import json
import time
import codecs
import sys
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
from datetime import date

import datetime

def dt(argu):
    return  datetime.datetime.fromtimestamp(argu/1000.0)


def get_self_events(params):
    request = requests.get("http://api.meetup.com/self/events",params=params)
    data1 = request.json()
    return data1

def get_events(params):
    request = requests.get("http://api.meetup.com/2/open_events",params=params)
    data1 = request.json()
    return data1

def get_member(param1):
    request = requests.get("http://api.meetup.com/2/member/12654048", params = param1)
    data = request.json()
    return data

def get_data():

    api_key = "xxx"
    param1={"key":api_key}
    data = get_member(param1)
    city_name = (data['city'])
    country_name = (data['country'])
    params = {"key":api_key, "city":city_name, "country": country_name, "radius": 50}
    response = get_events(params)
    return response

