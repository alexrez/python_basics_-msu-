s = input()
maxInt=None
digits=[]

while s:
	digits=[int(word) for word in s.split() if (word.isdigit() or (word[0]=='-' and word[1:].isdigit()))]
	tempInt=max(digits) if digits else None
	if maxInt==None:
		maxInt=tempInt
	elif tempInt!=None:
		maxInt =tempInt if maxInt<tempInt else maxInt
	s=input()


print(maxInt)