import sys
sys.path.append('..')
import requests
from auth.lsi import *

output=open("lithium_api_output.csv", "w+", encoding="UTF-8")

access_token = ACCESS_TOKEN
client_id = CLIENT_ID
response = requests.get(
    'https://api.lithium.com/lsi-data/v1/data/export/community/dell.prod',
    params={'fromDate': '20190801',
           'toDate': '20190802',
           'fields': 'user.login,user.community.role.name,board.title,request.geo.city,request.geo.country,request.device,request.headers.referrer.host'},
    auth=(access_token, ''),
    headers={'client_id': client_id,
            'Accept': 'text/csv'}
)

data = response.text

output.write(data)
