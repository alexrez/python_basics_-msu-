def PatternFind(seq, subseq):
	global len_p, len_s
	if len(seq)>=len_p:
		# pos=[seq.find(item[0], pos[-1]) for item in subseq]
		pos=[seq.find(subseq[0][0])]
		for i in range(1,len(subseq)):
			pos.append(seq.find(subseq[i][0], pos[-1]+subseq[i-1][1]+1))

		if -1 in pos:
			return -1
		for i in range(1, len(pos)):
			if pos[i]-1-subseq[i-1][1]!=pos[i-1]:
				return PatternFind(seq[pos[0]+pos[i]-1-subseq[i-1][1]-pos[i-1]:], subseq) or -1
		return pos[0] + len_s-len(seq)
	else:
		return -1

s=input()
p=input()
len_s=len(s)
len_p=len(p)
pattern=[]
for word in p.split('@'):
	if pattern and word=='':
		pattern[-1][1]+=1
	else:
		pattern.append([word, len(word)])

print(PatternFind(s, pattern))