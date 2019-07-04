#!/usr/bin/python
# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import re
import sys
import time

import requests

"""
<!doctype html>
<html>
  <head>
  <link href="/static/style.css" type="text/css" rel="stylesheet"/>
  <title>Driving to the target</title>
  </head>
  <h1>Driving to the target</h1>
  <body>
  <p>Hurry up, don\'t be late for you rendez-vous!
  <form method="get" action="/">
  <fieldset>
  <legend>Pick your direction</legend>
  <input type="number" name="lat" value="51.6498" min="-90" max="90" step="0.0001">
  <input type="number" name="lon" value="0.0982" min="-180" max="180" step="0.0001">
  <input style="display: none" name="token" value="gAAAAABdHeVGdZi6HrHJjNXjUTfRTpPHdjrlw65Vss4Awah2l5hChZLCEphtZ-cuFEFuwPQY763MeMNTMpWnrGDojQG8lHDFMtxvROBN2-zuzrzc5p38nMgAjnoPtKc188LjZThyFAHM">
  <button type="submit">go</button>
  </fieldset>
  </form>
  <p></p>
  </body>
</html>
"""
class MyHTMLParser(HTMLParser):
    lat = None
    lon = None
    token = None
    in_p = False
    ok = False
    p = ""
    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            cur_name = ""
            cur_value = ""
            for a in attrs:
                if a[0] == 'name':
                    cur_name = a[1]
                elif a[0] == 'value':
                    cur_value = a[1]
            if(cur_name == 'lat'):
                self.lat = cur_value
            if cur_name == 'lon':
                self.lon = cur_value
            if cur_name == 'token':
                self.token = cur_value
        elif tag == 'p':
            self.in_p = True
            self.ok = False
    def handle_data(self, data):
        if self.in_p:
            if 'You are getting closer' in data:
                self.ok = True
            self.p = data
    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_p = False

"""
You went 11m at a speed of 11km/h. You are getting away... UP (increasing)
You went 11m at a speed of 3km/h. You are getting closer... DOWN (decreasing)
You went 6m at a speed of 0km/h. You are getting away... W (increasing)
You went 13m at a speed of 0km/h. You are getting closer... E (decreasing)
"""

r = requests.get('https://drivetothetarget.web.ctfcompetition.com')
parser = MyHTMLParser()
while 1:
    parser.feed(r.text)
    lat = float(parser.lat)
    lon = float(parser.lon)

    print("%.5f,%.5f,%s,%s,%s" % (lat, lon, parser.token[:12], parser.token[12:], parser.ok))

    lat -= .00003
    lon -= .00003
    time.sleep(0.5)

    r = requests.get('https://drivetothetarget.web.ctfcompetition.com?lat=%.5f&lon=%.5f&token=%s' % (lat, lon, parser.token))
