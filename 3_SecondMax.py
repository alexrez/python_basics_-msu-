seq = eval(input())

max1=seq[0]
max2=None

for i in range(1, len(seq)):
	if seq[i]>max1:
		max2=max1
		max1=seq[i]
	elif seq[i]<max1:
		if max2==None or seq[i]>max2:
			max2=seq[i]


print(max2 if max2 else "NO")