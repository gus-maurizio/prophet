import itertools 
import numpy as np


coordinates = np.random.randint(10, size=(2,100))
points = set([ (coordinates[0][x],coordinates[1][x]) for x in range(len(coordinates[0]))])

# points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0)])
# points = set([(2,4),(4,2),(5,7),(7,5)]) # this is a rectangle not parallel to axis
#points = set([(1,1),(2,1),(3,1), (1,0), (2,0), (3,0),(2,4),(4,2),(5,7),(7,5)])
print(points)
rectangles = set()
inspected  = set()

def isParallel(rect):
	a,b,c,d = rect
	xa, ya = a
	xb, yb = b
	xc, yc = c
	xd, yd = d
	numx = len(set([xa,xb,xc,xd]))
	numy = len(set([ya,yb,yc,yd]))
	if numx == 2 and numy == 2:
		return True
	else:
		return False


def isSquareTriangle(a,b,c):
	# get coordinates of each point a, b, c
	xa, ya = a
	xb, yb = b
	xc, yc = c
	# for this to be a possible rectangle the distances (squared)
	# must be in pythagoras relationship
	ab = (xb - xa) ** 2 + (yb - ya) ** 2
	ac = (xc - xa) ** 2 + (yc - ya) ** 2
	bc = (xc - xb) ** 2 + (yc - yb) ** 2
	# find the largest distance
	distances = [ab, ac, bc]
	distances.sort(reverse=True, key=int)
	diagonal, sides = distances[0], distances[1:]
	if diagonal != sum(sides):
		return False, [a,b,c]
	# now compute the position of the point that will close the square
	# find which points are the diagonal and return them in order 
	if ab == diagonal:
		return True, [a,c,b]
	elif ac == diagonal:
		return True, [a,b,c]
	else:
		return True, [b,a,c]


def computePoint(triangle):
	"""
	Computes the last point D in an ABC square triangle 
	where a and c are the diagonal - triangle = [a,b,c]
	            D--- C
	            |  / |
	            | /  |
	            |/   |
	            A----B
	"""
	# get coordinates of each point a, b, c
	a, b, c = triangle
	xa, ya = a
	xb, yb = b
	xc, yc = c
	# due to subtriangle congruence
	xd = xc - (xb - xa)
	yd = (ya -yb) + yc
	d = (xd, yd)
	return d


triangles = set(itertools.combinations(points, 3))
totTriangles = len(triangles)
print('Total number of triangles: {}'.format(totTriangles))
nonRect = 0
yesRect = 0
for triangle in triangles:
	a, b, c = triangle
	print('inspecting triangle {} {} {}'.format(a,b,c))
	if frozenset([a,b,c]) not in inspected:
		inspected.add(frozenset([a,b,c]))
	else:
		yesRect += 1
		print('inspected')
		continue
	# are points part of a sqare triangle?
	isSquare, triangle = isSquareTriangle(a,b,c)
	if not isSquare:
		nonRect += 1
		continue
	yesRect += 1
	# candidate
	d = computePoint(triangle)
	if d in points:
		print('computed point {} for square triangle {} belongs to points set'.format(d, triangle))
		rectangles.add(frozenset([a,b,c,d]))
		inspected.add(frozenset([a,b,d]))
		inspected.add(frozenset([a,c,d]))
		inspected.add(frozenset([b,c,d]))
	else:
		print('computed point {} for square triangle {} not in points set'.format(d, triangle))

#--- print the rectangles and find if they are parallel to axis
numnonParallel = 0
for rect in rectangles:
	parallel = isParallel(rect)
	if not parallel:
		numnonParallel += 1
	print('rectangle parallel: {} {}'.format(parallel,rect))

#print(rectangles)
print('number of points is {} rectangles {} Total triangles {} non-Rect {} rect {}'.format(len(points),len(rectangles),totTriangles,nonRect,yesRect))
print('number of non parallel: {}'.format(numnonParallel))
