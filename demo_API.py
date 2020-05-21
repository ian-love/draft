########################################################################################################################
#
# demo_API.py
#
# Dump all my common stuff here and pull it in to any demo python files
#
########################################################################################################################
# Here's a list of available Meridian API
#
# https:/edit.meridianapps.com/api
# https:/edit.meridianapps.com/api/locations
# https:/edit.meridianapps.com/api/beacons/manage/auth?app_id={location_id}
# https:/edit.meridianapps.com/api/{location_id}/asset-beacons
# https:/edit.meridianapps.com/api/{location_id}/placemarks
# https://edit.meridianapps.com/api/locations/{Location ID}/placemarks/{Placemark ID}/image
#
#
import requests 
from requests.auth import HTTPBasicAuth 
import unicodecsv as csv 
import base64 
# Set variables for global use
username ='ian.love'
password ='pass'
mauth = HTTPBasicAuth(username, password)

class MeridianAPI:
	def __init__(self, apiuri, meridianlocation="", apiname="", location_id=""):
		self.apiuri = apiuri
		self.meridianlocation = meridianlocation
		self.apiname = apiname
		self.location_id = location_id
		
	def __str__(self):
		formURI = self.apiuri+self.meridianlocation+self.apiname+self.location_id
		return formURI
	
	def reqtoken(self):
		mytoken = requests.post(self,
                           {'password': password, 'email': username})
		print('\n\nMy Personal token for this session:', mytoken.json()['token'])
		return mytoken.json()['token']
	
	def mylocs(locuri):
		loc = requests.get(locuri,params=None,auth=mauth)
		return loc.json()['results']
		
	def convcsv(filename="", tocsv=[]):
		keys = tocsv.keys()
		with open(filename,'w') as csvfile:
			dict_writer = csv.DictWriter(csvfile, keys)
			dict_writer.writeheader()
			dict_writer.writerows(tocsv)
			
	def beacons(beaconsuri):
		numOfBeacons = requests.get(beaconsuri)
		print(numOfBeacons.url)
		print(numOfBeacons.json()['results'])
		typeOfBeacons = numOfBeacons.json()['results']
		print("'\n\n'{0} {1} {2}".format('There are',len(typeOfBeacons),'beacons'))
		for j in range(len(typeOfBeacons)):
			print('Beacon: ','type', typeOfBeacons[j]['type'],'MAC', typeOfBeacons[j]['mac'],'firmware is', typeOfBeacons[j]['firmware_a_version'],'hardware type',
				typeOfBeacons[j]['hw_type'], typeOfBeacons[j]['timestamp'])
		return typeOfBeacons
		
	def placemarks(placemarksuri):
		placemarks = requests.get(placemarksuri)
		locplacemarks = placemarks.json()['results']
		print("'\n\n'{0} {1} {2}.".format('This location has',len(locplacemarks),'placemarks'))
		for i in range(len(locplacemarks)):
			print('Placemark: ', locplacemarks[i]['name'],'is landmark ', locplacemarks[i]['landmark'],' x coordinate: ', locplacemarks[i]['x'], ' y coordinate: ', locplacemarks[i]['y'])
		return locplacemarks
