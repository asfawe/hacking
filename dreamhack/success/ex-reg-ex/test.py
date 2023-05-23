import re

input_val = "dr12345e1am@aaa.a"

m = re.match(r'dr\w{5,7}e\d+am@[a-z]{3,7}\.\w+', input_val)

if m:
	print("Hello, world!")
else:
	print("No!!!!!!!!")