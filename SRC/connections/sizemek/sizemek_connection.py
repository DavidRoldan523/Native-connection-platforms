import requests
import credentials as credential
from requests.auth import HTTPBasicAuth

r = requests.get('https://api.sizmek.com/rest/login/login',
                 auth=HTTPBasicAuth(credential.username, credential.password),
                 headers={'Accept': 'application/json',
                          'Content-Type': 'application/json'},
                 timeout=10)

print(r.status_code)


