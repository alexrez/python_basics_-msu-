def Palindrom(x, k):
	if x<10:
		return True
	else:
		return x%10 == x//(10**(k-1)) and Palindrom(x%(10**(k-1))//10, k-2)
	
def razr(x):
	return 1 if x<10 else razr(x//10) + 1

number = int(input())
if (number%10):
	n = razr(number)
	print("YES" if Palindrom(number, n) else "NO")
else:
	print("NO")