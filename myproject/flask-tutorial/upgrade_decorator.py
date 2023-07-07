from functools import wraps

def deco(func):
	print("d")
	@wraps(func)
	def f(*args, **kwargs):
		print("f")
		print(*args, **kwargs)
		return func(*args, **kwargs)
	return f

@deco
def double(num):
	return 2*num

print(double(1))
print(double)

# def deco(func):
#     print("d")
#     def f(*args, **kwargs):
#         print("f")
#         return func(*args, **kwargs)
    
#     def g(*args, **kwargs):
#         print("g")
#         return func(*args, **kwargs)
    
#     return g

# @deco
# def double(num):
#     return 2*num

# double(3)