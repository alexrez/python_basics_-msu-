lab = eval(input())

def go_through_lab(l):
	global m
	n=len(l)
	walk=[n-1]
	path = set()
	while(walk):
		ex = walk.pop()
		if ex == 0:
			return True
		else:
			path.add(ex)
			stop = min(ex+1, m+1)
			for ind in range (1, stop):
				if l[ex-ind]==ind:
					if ex-ind+1 not in path:
						walk.append(ex-ind+1)
					if ex-ind not in path:
						walk.append(ex-ind)
	return False

m=max(lab)

print("YES" if go_through_lab(lab) else "NO")