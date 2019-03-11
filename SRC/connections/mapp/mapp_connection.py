import requests

r = requests.get('https://webdomain/api/rest/v10',
                 headers={'Authorization:': 'Basic dGVzdEB0ZXN0LmNvbTpBUEkgdXNlcg',
                          'Accept': 'application/json',
                          'Content-Type': 'application/json'},
                 timeout=15)

print(r.status_code)
