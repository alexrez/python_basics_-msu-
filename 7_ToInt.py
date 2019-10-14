def toint(foo):
	def int_foo(*args):
		# new_args =[]
		# for el in args:
		# 	if type(el) is float:
		# 		el = int(el)
		# 	new_args.append(el)
		new_args = [int(el) if type(el)==float else el for el in args]
		res = foo(*new_args)
		if type(res) is float:
			res = int(res)
		return res
	return int_foo

# @toint
# def root(x):
# 	return x**0.5

# print(root(11.8))

# @toint
# def dou(x):
#     return x*2

# print(dou(11.8))
# print(dou(11))
# print(dou("11"))
# print(dou((11,11)))

# @toint
# def mull(x, y):
# 	return x*y

# print(mull(11.8,12.12))
# print(mull("12",12.12))
# print(mull(12.12,(1,2)))
# print(mull(11.5+0j,12.12))
# print(mull(11.5+1.5j,12.12))	