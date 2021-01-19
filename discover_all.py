import requests

headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
           "Authorization": "Bearer BQCHd-FxIW64oFroTK9kQw2x-hckPBikuBHhLZNcQ9nLmTVaNqdfW1g-J8T8DOh9kkoVeuRMt9_TaIuCmpExSq64fwsAvOZjyeGSjAf14_oeL4hljet5n2nJZjbZxPUrcR3u7ENQGcPaPpghQg"}
url = 'https://api.spotify.com/v1/artists//albums'
data1 = requests.get(url, headers=headers).json()
print(data1)
