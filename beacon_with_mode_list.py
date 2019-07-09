########################################################################################################################
#
# 11mar 2019
# script to list beacon mac, associated map and beacon name
# "C:\DATA\OneDrive - Hewlett Packard Enterprise\meridian\scripts\working\KSC_beacon_list.py"

	# // start //
	# // end //
########################################################################################################################
# Load the meridianAPI.py module
import requests
from demo_API import *

# Meridian location ID dictionary of all locations I'm authorized in
meridianLocation = {
"TSS_hague":"6695066221936640",
"my_site":"5158295536926720",
"cspo":"5794256550100992",
"reimagine":"5204712926740480",
"atm":"5819981480067072",
"Terna" : "5673887759335424",
"TSS_2019":"6314911219056640",
"lyngsoe":"5200230666731520",
"jbs" : "4518368792543232",
"ksc" : "5710137816252416"}

# list of endpoints
endpoints = {
"beacons":"/beacons?page_size=500",
"placemarks":"/placemarks",
"token":"/tokens",
"login":"/login",
"logout":"/logout",
"locations":"/locations",
"maps":"/maps",
"organizations":"/organizations"}

# URLs will be needed to communicate with Meridian's API on the regular server
apiURI = "https://edit.meridianapps.com/api/locations/"
loginURI = "https://edit.meridianapps.com/api/login"

# URLs will be needed to communicate with Meridian's API on the EU server
eu_apiURI = "https://edit.meridianapps.com/api/locations/"
eu_loginURI = "https://edit.meridianapps.com/api/login"

# which site ??
testloc = meridianLocation["ksc"]
tokid = MeridianAPI.reqtoken(loginURI)


beaconEndpoint = endpoints["beacons"]
beaconURI = MeridianAPI(apiURI, testloc, beaconEndpoint)
print (beaconURI)

beacons = requests.get(beaconURI)
locbeacons = beacons.json()['results']

for i in range(len(locbeacons)):
		 print(locbeacons[i]['mac'],'is a',locbeacons[i]['type'],'on floormap',locbeacons[i]['map'],'with a name of',locbeacons[i]['name'],'linked with campaign',locbeacons[i]['enter_campaigns'])