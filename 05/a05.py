from pyquery import PyQuery as pq
import requests
import sys
import time


iteration = 0
lat = 0
lon = 0
min_lat = -90.0
max_lat = 90.0
min_lat = -180.0
max_lat = 180
token = ""


def get_token(html):
    doc = pq(html)
    x = doc("input[name=token]")
    # print("tok:", x.attr.value)
    return x.attr.value

def get_lat(html):
    doc = pq(html)
    x = doc("input[name=lat]")
    # print("lat:", float(x.attr.value))
    return float(x.attr.value)

def get_lon(html):
    doc = pq(html)
    x = doc("input[name=lon]")
    # print("lon:", float(x.attr.value))
    return float(x.attr.value)

def get_hint(html):
    doc = pq(html)
    x = doc("p:last")
    # print("hint",x.text())
    return x.text()

def last_lat(x):
    with open("lat.txt",'w') as o:
        o.write(str(x))

def last_lon(x):
    with open("lon.txt",'w') as o:
        o.write(str(x))



# get initial token
response = requests.get("https://drivetothetarget.web.ctfcompetition.com/")
# print(response.text)
token = get_token(response.text)
lat = get_lat(response.text)
lon = get_lon(response.text)

# print("initial:")
# print(lat, lon, token)

too_fast = False
# lat_step = 0.00003
lat_step = -0.00003
lon_step = 0.00003

while True:
    # print("STEP " + "-"*80)

    # print(lat)
    lat = float(lat) + float(lat_step)
    lon = float(lon) + float(lon_step)
    # print(lat)

    url = "https://drivetothetarget.web.ctfcompetition.com/?"
    url += "lat=" + str(lat)
    url += "&lon=" + str(lon)
    url += "&token=" + token

    response = requests.get(url)
    # print(response.text)
    token = get_token(response.text)
    lat = get_lat(response.text)
    lon = get_lon(response.text)
    hint = get_hint(response.text)
    print(lat_step, lat, lon, hint)

    # print("\t",hint)

    # if "this is too fast!" in hint:
    #     lat_step = lat_step - 0.00001
    #     too_fast = True

    # if "You are getting closer" in hint:
    #     lat_step = lat_step + 0.00001
    
    # if "You are getting away" in hint:
    #     lat_step = lat_step * -1.0
    #     # lon_step = lon_step * -1.0

    # if not too_fast:
    #     print("accelerating by 0.00001")
    #     lat_step = lat_step + 0.00001
    last_lat(lat)
    last_lon(lon)

    time.sleep(0.1)

