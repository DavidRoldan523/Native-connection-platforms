import requests

r = requests.get('https://webdomain/api/rest/v10',
                 headers={'Authorization:': 'Basic anVhbi5lc3Bpbm9zYUBhcmlhZG5hY2cuY29tOkFyaWFkbmFlc3Bpbm9zYTAyMTMh',
                          'Accept': 'application/json',
                          'Content-Type': 'application/json'},
                 timeout=15)

print(r.status_code)
