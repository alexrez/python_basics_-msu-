def update_dict(d, man_1, man_2):
	if not(man_1 in d):
		d.update({man_1: {man_2}})
	else:
		d[man_1].add(man_2)
	if not(man_2 in d):
		d.update({man_2: {man_1}})
	else:
		d[man_2].add(man_1)

guys = eval(input())
friendship = {}

while guys[0] or guys[1]:
	update_dict(friendship, guys[0], guys[1])
	guys = eval(input())

all_known = []

for man, friends in friendship.items():
	if len(friends) == len(friendship)-1:
		all_known.append(man)

print(*(all_known) if all_known else '\n')