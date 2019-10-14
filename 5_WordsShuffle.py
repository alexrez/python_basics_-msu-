def StrCmp(str1, str2):
	global kodec
	words1=sorted(str1.split())
	words2=sorted(str2.split())
	zpt=[[], []]
	counter=0
	if len(words1)!=len(words2):
		return False
	for word in zip(words1, words2):
		if word[0]!=word[1]:
			if not word[0].isalpha() or not word[1].isalpha():
				if len(word[0])==len(word[1]):
					for letter in zip(word[0], word[1]):
						if letter[0]!=letter[1]:
							if letter[0].isalpha() or letter[1].isalpha():
								return False
							else:
								zpt[0].append(letter[0])
								zpt[1].append(letter[1])
				else:
					stop=min(len(word[0]), len(word[1]))
					i=0 if len(word[0])>len(word[1]) else 1
					if word[0][:stop]!=word[1][:stop] or word[i][stop:].isalpha():
						return False
					for z in word[i][stop:]:
						zpt[i].append(z)
			else:
				return False
	return counter==0 and sorted(zpt[0])==sorted(zpt[1])

s1 = input().lower()
s2 = input().lower()

if len(s1)!=len(s2):
	print(False)
else:
	print(StrCmp(s1, s2))