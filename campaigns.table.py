########################################################################################################################
#
# Build a table showing the placemark and the map ID where it is seen
#
# 3may 2018
#
########################################################################################################################
import requests
from requests.auth import HTTPBasicAuth
import unicodecsv as csv
import base64
from meridianAPI import *

campaignURL = "https://edit.meridianapps.com/api/locations/5819981480067072/campaigns"

campaigns = requests.get(campaignURL)
locplacemarks = campaigns.json()['results']

print("'\n\n'{0} {1} {2}.".format('This location has',len(locplacemarks),'campaigns'))
for i in range(len(locplacemarks)):
		 print(locplacemarks[i]['title'],'campaign uses beacon with MAC address',locplacemarks[i]['beacons'],'with campaign mode of',locplacemarks[i]['type'],'and the message is',locplacemarks[i]['message'])