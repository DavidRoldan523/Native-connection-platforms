import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://staging11.shortest-route.com/qatest/api/rest/rest/v10/user/get',
                 auth=HTTPBasicAuth('lech.zawistowski@mapp.com', 'Dokiva&2'),
                 headers={'Accept': 'application/json',
                          'Content-Type': 'application/json'},
                 timeout=10)

print(r.status_code)


