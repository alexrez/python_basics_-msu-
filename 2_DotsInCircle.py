def InCircle(x0, y0):
	if x0 or y0:
		x1, y1 = eval(input())
		return ((x0-x)**2+(y0-y)**2)**0.5<=r and InCircle(x1, y1)
	else: return True


x, y, r = eval(input())
x1, y1 = eval(input())
print ("YES" if InCircle(x1, y1) else "NO")