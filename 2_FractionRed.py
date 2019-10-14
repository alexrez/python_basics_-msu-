def delim(a, b):
	if a!=0 and b!=0:
		if a > b:
			a = a%b
		else:
			b = b%a
		return delim(a, b)
	else: return a+b

def frac(m, n):
	if n%m == 0:
		return 1, n//m
	else:
		k = delim(m, n)
		return m//k, n//k
		

a, b = eval(input())
if (a>b):
	print(a//b, end =" ")

print('{0}/{1}'.format(*frac(a%b, b)) if a%b else " ")