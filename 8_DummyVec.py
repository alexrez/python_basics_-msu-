class vector:
	def __init__(self, v):
		self.vec = [i for i in v]

	def __str__(self):
		s=""
		for i in self.vec:
			s+="{}:".format(i)
		return s[:-1]

	def __add__(self, vec2):
		if isinstance(vec2, vector):
			return vector(i+j for i, j in zip(self.vec, vec2.vec))
		else:
			return vector(i+j for i, j in zip(self.vec, vec2))

	__radd__ = __add__

# a, b = vector([2,1,2,1,2,1,2,1]), vector(range(8))
# print(a, b, a+b, b+range(8), range(8)+b)