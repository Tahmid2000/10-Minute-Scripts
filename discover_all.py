import requests

headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
           "Authorization": "Bearer "}
url = 'https://api.spotify.com/v1/artists//albums'
data1 = requests.get(url, headers=headers).json()
print(data1)
