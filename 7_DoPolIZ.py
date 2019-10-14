operation = {'+', '-', '*'}
stack = [i for i in input().split() if i.isdigit() or (i[0]=='-' and i[1:].isdigit()) or i in operation]

def poliz(op, st):
	a = st.pop()
	if a in operation:
		a = poliz(a, st)
	b = st.pop()
	if b in operation:
		b = poliz(b, st)
	r = eval(str(b)+op+str(a))
	return r

mode = stack.pop()
if mode in operation:
	print(poliz(mode, stack))
else:
	print(mode)