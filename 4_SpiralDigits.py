import pprint
n, m=eval(input())
arrow=['left', 'down', 'right', 'up']
mat = [[-1 for _ in range(n)] for _ in range(m)]
cur = [0, 0, 0]
for ind in range(n*m):
	mat[cur[0]][cur[1]]=ind%10
	
	if (cur[2]==0 and cur[1]==n-1-cur[0]) or (cur[2]==1 and cur[0]==m-n+cur[1]) or (cur[2]==2 and cur[1]==m-1-cur[0]) or (cur[2]==3 and cur[0]==cur[1]+1):
		cur[2]=(cur[2]+1)%4

	if cur[2]<2:
		cur[(cur[2]+1)%2]+=1
	else:
		cur[(cur[2]+1)%2]-=1

	
	
for line in mat:
	print(*(line))