import util, ds_stl



# turn each point into a little triangle
def cloud_to_triangles(points):
	size = 0.1
	tri = [[0,0,0], [0,size,0], [size,0,0]]
	translate = lambda x, y, z: [[x+x1, y+y1, z+z1] for x1,y1,z1 in tri]
	return [translate(*p) for p in points]


# turn each point into a little tetrahedron
def cloud_to_triangles2(points):
	size = 0.1
	tetra = [[[0,0,0], [0,1,0], [1,0,0]],  [[0,0,0], [1,0,0], [0,0,1]], [[0,0,0], [0,0,1], [0,1,0]], [[1,0,0], [0,1,0], [0,0,1]]]

	translate = lambda x, y, z: [[[x+x1*size, y+y1*size, z+z1*size] for x1,y1,z1 in tri] for tri in tetra ]
	return util.flatten([translate(*p) for p in points])

# generate a test file to see how the equation looks
def test_eq(eq, num):
	points = [eq(util.get_rand_coordinate()) for _ in range(num)]
	triangles = cloud_to_triangles2(points)
	ds_stl.save_stl('test_eq.stl', triangles)


test = [[0,0,0], [100,0,0]]

print(cloud_to_triangles2(test))