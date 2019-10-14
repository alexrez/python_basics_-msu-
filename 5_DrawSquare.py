def squares(*args):
	w=args[0]
	h=args[1]
	sq=[bytearray(b'.'*w) for _ in range(h)]
	data=list(args[2:])
	for info in data:
		for i in range(info[1], info[1]+info[2]):
			sq[i][info[0]:info[0]+info[2]]=[ord(info[3]) for _ in range(info[2])]
	for line in sq:
		print(line.decode('UTF-8'))



# squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))