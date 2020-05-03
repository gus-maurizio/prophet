points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0)])
# points = set([(2,4),(4,2),(5,7),(7,5)]) # this is a rectangle not parallel to axis
print(points)
rectangles = set()

for p in points:
	for c in points:
		x,y = p
		v,w = c
		if x == v or y == w:
			continue
		if (x,w) in points and (v,y) in points:
				if frozenset([p,c,(x,w),(v,y)]) not in rectangles:
					print('{} is a new rectangle'.format([p,c,(x,w),(v,y)]))
					rectangles.add(frozenset([p,c,(x,w),(v,y)]))
print(rectangles)
print('number of rectangles is {}'.format(len(rectangles)))
		
