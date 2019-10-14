def moar(a, b, n):
	count=0
	for elem in a:
		if elem%n==0:
			count+=1

	for elem in b:
		if elem%n==0:
			count-=1

	return True if count>0 else False
