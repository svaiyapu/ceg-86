#!/usr/bin/env python
import urllib
from collections import defaultdict
import json

d = defaultdict(list)
# get distinct location values
with open('g.in','r') as f:
    for line in f:
        l = line.split('|')[-1].strip().lower()
        d[l] = []

# attempt to geocode them
url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&%s"
for l in d.keys():
    u = url % urllib.urlencode([("address",l)])
    print u
    try:
        data = json.loads(' '.join([line.strip() for line in urllib.urlopen(u).readlines()]))
        if data["status"] == "OK":
            d[l].append(data["results"][0]["formatted_address"])
            d[l].append(data["results"][0]["geometry"]["location"]["lat"])
            d[l].append(data["results"][0]["geometry"]["location"]["lng"])
    except:
        pass

# output, appending formatted location, lat, long
with open('g.in','r') as f:
    with open('g.out','w') as o:
        for line in f:
            l = line.split('|')[-1].strip().lower()
            if not len(d[l]) > 0:
                l = "india"
            oline = "|".join([line.strip(), d[l][0], "%0.7f" % d[l][1], "%0.7f" %d[l][2]])
            o.write(oline+"\n")
