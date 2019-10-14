import collections

class DefCounter(collections.Counter):
	def __init__(self, *args, **kwargs):
		if 'missing' in kwargs:
			self.__missing = kwargs.pop('missing')
		else:
			self.__missing = -1
		super().__init__(*args, **kwargs)

	def __getitem__(self, key):
		if key not in self:
			return self.__missing
		else:
			return super().__getitem__(key)

	


# A = DefCounter("QWEqweQWEqweQWE", missing=-10)
# print(A)
# print(A["Z"])
# A["P"]+=5
# print(A)

# A = DefCounter(range(10))
# print(A)
# print(A[5],A[15])

# A = DefCounter(a=2,b=3,c=8,missing=2)
# print(A["a"], A["c"], A["f"])