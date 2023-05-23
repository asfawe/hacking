import requests

r = requests.get('http://natas15.natas.labs.overthewire.org/')

print(r.text)