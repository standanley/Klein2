''' coordinates are [u,v], points are [x,y,z] '''

import math, random
import util, tests
random.seed(0)

def sphere_eq(c):
	u,v = c
	x = math.cos(u)*math.sin(v/2)
	y = math.sin(u)*math.sin(v/2)
	z = -math.cos(v/2)
	return [x,y,z]

def klein_eq(c):
	u,v = c
	# todo - check bounds on u,v

	h = 15
	w = 5
	r1 = .5 #2
	r2 = 3 #5 #5

	r = r1 + (r2-r1)*(math.sin(u+math.sin(u)/2)+1)/2
	# math.atan2(dzdu, dxdu), assuming r constant
	dzdu = h*math.cos(u/2)/2
	dxdu = w*-math.cos((1-math.cos(u/2))*math.pi) * math.sin(u/2)*math.pi/2
	a = math.atan2(dzdu, dxdu)
	#print(u, a)

	x = w*-math.sin((1-math.cos(u/2))*math.pi) + r*math.sin(a)*math.cos(v)
	y =                                          r*math.sin(v)
	z = h*math.sin(u/2)                        + r*-1*math.cos(a)*math.cos(v)
	return [x,y,z]

for ui in range(0, 50):
	u = 2*math.pi*ui/50
	klein_eq([u, 0])
tests.test_eq(klein_eq, 10000)
