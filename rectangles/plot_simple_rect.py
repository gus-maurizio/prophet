import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(24.0, 12.0))
plt.title('Elementary Case')

# points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0)])
# points = set([(2,4),(4,2),(5,7),(7,5)]) # this is a rectangle not parallel to axis
# points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0),(2,4),(4,2),(5,7),(7,5)])

coordinates = np.random.randint(30, size=(2,90))
points = set([ (coordinates[0][x],coordinates[1][x]) for x in range(len(coordinates[0]))])



print(points)
rectangles = set()

x = [x[0] for x in points]
y = [x[1] for x in points]

plt.scatter(x, y, color='green')


for p in points:
	for c in points:
		x,y = p
		v,w = c
		if x == v or y == w:
			continue
		if (x,w) in points and (v,y) in points:
				if frozenset([p,c,(x,w),(v,y)]) not in rectangles:
					# print('{} is a new rectangle'.format([p,c,(x,w),(v,y)]))
					rectangles.add(frozenset([p,c,(x,w),(v,y)]))
					_rect = plt.Polygon([list(p), [x,w], list(c), [v,y]], fill=True, edgecolor='r', alpha=0.2)
					plt.gca().add_patch(_rect)



plt.axis('equal')
plt.grid(axis='both', which='both')
plt.show()


print(rectangles)
print('number of rectangles is {}'.format(len(rectangles)))
		
