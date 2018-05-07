########################################################################################################################
#
# Build a table showing the placemark and the map ID where it is seen
#
# 2may 2018
#
########################################################################################################################
import requests
from requests.auth import HTTPBasicAuth
import unicodecsv as csv
import base64
from meridianAPI import *

placemarkURL = "https://edit.meridianapps.com/api/locations/5819981480067072/placemarks"

placemarks = requests.get(placemarkURL)
locplacemarks = placemarks.json()['results']

print("'\n\n'{0} {1} {2}.".format('This location has',len(locplacemarks),'placemarks'))
for i in range(len(locplacemarks)):
		 print(locplacemarks[i]['name'],'is on map', locplacemarks[i]['map'])