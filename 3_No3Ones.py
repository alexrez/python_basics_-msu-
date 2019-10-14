nn = int(input())

l = [0 for i in range(nn+1)]

def quantity(n):
	if n==3:
		return 7
	elif n==4:
		return 13
	elif n==5:
		return 24
	elif l[n]> 0:
		return l[n]
	else:
		l[n] = quantity(n-3)+quantity(n-2)+quantity(n-1)
		return l[n]

print(quantity(nn))