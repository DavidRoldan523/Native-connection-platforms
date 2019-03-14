import requests
import credentials as credential
from requests.auth import HTTPBasicAuth

r = requests.get('https://staging11.shortest-route.com/qatest/api/rest/rest/v10/user/get',
                 auth=HTTPBasicAuth(credential.email, credential.password),
                 headers={'Accept': 'application/json',
                          'Content-Type': 'application/json'},
                 timeout=10)

print(r.status_code)


