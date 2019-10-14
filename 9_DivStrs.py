class DivStr(str):
	def __init__(self, val):
		self.s = val
		self.len = len(val)

	def __floordiv__(self, parties):
		l = self.len // parties
		return [self.s[i*l:(i+1)*l] for i in range(parties)]

	def __mod__(self, rem):
		r = self.len % rem
		return self.s[self.len-r:]


# a = DivStr("XcDfQWEasdERTdfgRTY")
# print(*a//4)
# print(a%4)