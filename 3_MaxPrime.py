import math

n = int(input())
if n%2==0:
	n-=1
if n==1:
	print(2)

while n>1:
	i=3
	while i< int(math.sqrt(n))+2:
		if n%i==0:
			break
		i+=1
	else:
		print(n)
		break
	n-=2
