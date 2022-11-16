import requests

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://localhost:8888/processing.php", data=params)
print(r.text)