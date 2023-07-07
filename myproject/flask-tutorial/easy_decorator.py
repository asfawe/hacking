def deco(func):
	print("deco! a~~~")
	return func

def double(num):
	return 2*num

double = deco(double)
print(double(1))