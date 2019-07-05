from pyquery import PyQuery as pq
import requests
import sys
import time
import datetime

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

def is_closer(hint):
    if "closer" in hint:
        return True
    else:
        return False


# get initial token
response = requests.get("https://drivetothetarget.web.ctfcompetition.com/")
# print(response.text)
token = get_token(response.text)
lat = get_lat(response.text)
lon = get_lon(response.text)

# print("initial:")
# print(lat, lon, token)

too_fast = False
# lat_step = -0.00003
# lon_step =  0.00003

lat_step = 0.00003
lon_step = 0.00003

direction_changes = 0
lat_bounce = 0
lon_bounce = 0


with open("output_a05.txt","a") as out:
    c = 0
    out.write("timestamp|counter|lat|long|hint|token\n")
    while True:
        c += 1

        # two step process - 
        #   adjust lat and check if closer
        #   adjust lon and check if closer


        # ----------------------------------------------
        # adjust lat and check if closer
        # ----------------------------------------------
        lat = float(lat) + float(lat_step)

        url = "https://drivetothetarget.web.ctfcompetition.com/?"
        url += "lat=%.5f" % lat
        url += "&lon=%.5f" % lon
        url += "&token=" + token
        response = requests.get(url)
        token = get_token(response.text)
        lat = get_lat(response.text)
        lon = get_lon(response.text)
        hint = get_hint(response.text)

        if "away" in hint:
            lat_step = lat_step * -1
            direction_changes += 1
            lat_bounce += 1
            print("changing lat direction", lat_step)

        # output
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        output = "%s|%-5s|%-10s|%-10s|%s|%s" % (st, str(c), lat, lon, hint, token)
        print(lat_step, lon_step, output)
        output = "%s|%-5s|%-10s|%-10s|%s|%s\n" % (st, str(c), lat, lon, hint, token)
        out.write(output)

        if lat_bounce > 5:
            print("lat is bouncing.  setting step to 0")
            lat_step = 0


        # ----------------------------------------------
        #   adjust lon and check if closer
        # ----------------------------------------------

        lon = float(lon) + float(lon_step)

        url = "https://drivetothetarget.web.ctfcompetition.com/?"
        url += "lat=%.5f" % lat
        url += "&lon=%.5f" % lon
        url += "&token=" + token
        response = requests.get(url)
        token = get_token(response.text)
        lat = get_lat(response.text)
        lon = get_lon(response.text)
        hint = get_hint(response.text)


        if "away" in hint:
            lon_step = lon_step * -1
            direction_changes += 1
            lon_bounce += 1
            print("changing lon direction", lon_step)

        # output
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        output = "%s|%-5s|%-10s|%-10s|%s|%s" % (st, str(c), lat, lon, hint, token)
        print(lat_step, lon_step, output)
        output = "%s|%-5s|%-10s|%-10s|%s|%s\n" % (st, str(c), lat, lon, hint, token)
        out.write(output)

        if lon_bounce > 5:
            print("lon is bouncing.  setting step to 0")
            lon_stop = 0


        if lat_bounce == 0 and lon_bounce == 0:
            print("We've bracketed the Bismark!")
            sys.exit(0)

        time.sleep(0.1)

