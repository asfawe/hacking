import requests
from http.cookies import SimpleCookie

url = 'http://host3.dreamhack.games:22327/user/account'

for i in range(0, 86400000):

	data = {'guest' : 'guest'}
	r = requests.post(url, data=data)
	print(r.cookies)
	r = requests.get("http://host3.dreamhack.games:22327/description.jpg")
	print(r.headers)
	print(r.cookies)

	# print(r.text)
	# if 'fail' not in r.text:
	# 	print(f'admin Password : {i}')
	# 	break