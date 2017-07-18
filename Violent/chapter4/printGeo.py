import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def printRecord(tgt):
	rec = gi.record_by_addr(tgt)
	city = rec['city']
	postal = rec['postal_code']
	country = rec['country_name']
	lon = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: '+tgt +'Geo-located.'
	print '[+] '+str(city)+','+str(postal)+','+str(country)
	print '[+] Latitude: '+str(lat)+',Longitude: '+str(lon)
tgt = '173.255.226.98'
printRecord(tgt)