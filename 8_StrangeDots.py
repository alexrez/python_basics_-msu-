import sys

class Dots:
	def __init__(self, a, b):
		self.x1 = float(a)
		self.x2 = float(b)

	def __str__(self):
		return ("{} {}".format(self.x1, self.x2))

	def __getitem__(self, key):
		if isinstance(key, int):
			return [self.x1+i*(self.x2-self.x1)/(key-1) for i in range(key)]

		start, stop, qua = key.start or 0, key.stop or key.step, key.step
		# print(start, stop, qua)
		extra = 0
		st = 0

		if start >= stop:
			extra += start - stop + 1

		if start < 0:
			st = start
			extra -= start
			start = 0

		if qua == None:
			qua = stop
			sl = [self.x1+i*(self.x2-self.x1)/(qua-1) for i in range(st, qua+extra)]
			return sl[start]

		if stop > qua:
			extra += stop - qua

		sl = [self.x1+i*(self.x2-self.x1)/(qua-1) for i in range(st, qua+extra)]
		return [sl[i] for i in range(start, stop-st)]

# a = Dots(-1,1)
# print(*a[7])
# print(a[0:7])
# print(a[2:7])
# print(a[4:7])
# print(a[7:7])
# print(a[-7:7])
# print(*a[1:3:7])
# print(*a[:3:7])
# print(*a[2::7])
# print(*a[::7])
# print(*a[-2:8:7])

# a = Dots(0,40)
# print(*a[5])
# print(a[0:5])
# print(a[2:5])
# print(a[4:5])
# print(a[7:5])
# print(a[-7:5])
# print(*a[1:3:5])
# print(*a[:3:5])
# print(*a[2::5])
# print(*a[::5])
# print(*a[-2:6:5])