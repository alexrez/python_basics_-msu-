import collections
c = collections.Counter()
text = input().lower().split()
while text:
	for word in text:
		c[word]+=1
	text = input().lower().split()

print(c.most_common(1)[0][0] if len(c)==1 or c.most_common(2)[0][1]!=c.most_common(2)[1][1] else '---')