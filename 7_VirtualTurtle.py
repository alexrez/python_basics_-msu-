def turtle(coord, direction):
	x = coord[0]
	y = coord[1]
	moove = yield
	while moove:
		if moove=='f':
			if direction==0:
				x+=1
			elif direction==1:
				y+=1
			elif direction==2:
				x-=1
			else:
				y-=1
		elif moove=='l':
			direction = (direction+1)%4
		elif moove=='r':
			direction = (direction-1)%4
		moove = yield (x, y)

# robo = turtle((0,0),0)
# start = next(robo)
# for c in "flfrffrffr":
# 	print(*robo.send(c))


# "f" (переход на 1 шаг вперёд), "l" (поворот против часовой стрелки на 90°) и "r" (поворот по часовой стрелке на 90°) 