import json
import requests
from pprint import pprint
# 06d8e30f58a8ce0a31036c560289c5e18c088c60
url = 'https://wger.de/api/v2/exerciseinfo'
data = '{"key": "value"}'
headers = {'Accept': 'application/json',
                  'Authorization': 'Token 06d8e30f58a8ce0a31036c560289c5e18c088c60'}
r = requests.patch(url=url, data=data, headers=headers)
r
r.content
pprint(json.loads(r.content))