import requests
from urllib.parse import urlencode, unquote, quote_plus
import requests

def find_smokectr():

	addr = []

	page = '1'
	perPage = '100'
	returnType = 'JSON'
	serviceKey = 'FM1hqdeJkwNfMm%2B%2FvUTZpYHGCtdnD%2BKs8gLCIk6p0rft8tFL6krZSWyb8p%2BxTb1hThPcIjh9mubEaK4DKGZZZg%3D%3D'
	
	url = "https://api.odcloud.kr/api/15018867/v1/uddi:20e4afd6-ccb0-4e2f-a6f9-ab2fdaae63f0_201704120940?page=" \
	+ page +"&perPage=" + perPage + "&returnType="+ returnType + \
	"&serviceKey=" + serviceKey

	get_data = requests.get(url)

	data = get_data.json()


	for num in data['data']:
		addr.append(num['주소'])

	return addr

def find_dimctr(sigun_nm):

	logt = []
	lat = []
	result = []

	url = "https://openapi.gg.go.kr/ImbecilityConsultationCenter"
	KEY = '280c95a3f2c34916acf47163f4739ddf'
	Type = 'json'
	pIndex = '1'
	pSize = '100'
	SUM_YY = ''
	SIGUN_NM = sigun_nm
	SIGUN_CD = ''
	
	
	queryParams = '?' + urlencode({ 
		quote_plus('KEY') : KEY, 
		quote_plus('Type') : Type, 
		quote_plus('pIndex') : pIndex, 
		quote_plus('pSize') : pSize, 
		quote_plus('SUM_YY') : SUM_YY, 
		quote_plus('SIGUN_NM') : SIGUN_NM,
		quote_plus('SIGUN_CD') : SIGUN_CD,
		})

	get_data = requests.get(url+queryParams)

	data = get_data.json()

	result = data['ImbecilityConsultationCenter'][1]['row']


	# for key in data['ImbecilityConsultationCenter'][1]['row']:
	# 	logt.append(key['REFINE_WGS84_LOGT'])
	# 	lat.append(key['REFINE_WGS84_LAT'])

	# return dict(zip(logt, lat))
	return result