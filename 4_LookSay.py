def LookSay():
	seq=[1]
	yield seq[0]
	while(True):
		k=1
		last=seq[0]
		result=[]
		for i in range(1,len(seq)):
			if last==seq[i]:
				k+=1
			else:
				result.append(k)
				result.append(last)
				k=1
			last = seq[i]
		result.append(k)
		result.append(last)
		for _ in result:
			yield _
		seq=result
