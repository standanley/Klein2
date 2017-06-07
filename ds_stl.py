''' DanStan's own STL output '''
import struct

def make_triangle(triangle):
	return [0,0,0]+[xyz for point in triangle for xyz in point ] + [0]

def flatten(x):
	return [float(z) for y in x for z in y]

# [[[x1a, y1a, z1a], [x1b, ...], [x1c, ...]],  [[x2a, ...], ...], ...]
def save_stl(filename, triangles):
	format_str = '<'+'b'*80+'i'+'ffffffffffffe'*len(triangles)
	stuff = flatten([make_triangle(tri) for tri in triangles])
	#print(stuff)
	stuff2 = [0]*80+[len(triangles)]+stuff
	#print(stuff2)
	output = struct.pack(format_str, *(stuff2))
	#print(output)
	f = open(filename, 'wb')
	f.write(output)
	f.close()

def test_ds_stl():
	#triangles = [[[0,0,0], [0,1,0], [1,0,0]]]
	# XY, XZ, YZ, XYZ
	triangles = [[[0,0,0], [0,1,0], [1,0,0]],  [[0,0,0], [1,0,0], [0,0,1]], [[0,0,0], [0,0,1], [0,1,0]], [[1,0,0], [0,1,0], [0,0,1]]]
	save_stl('test_ds.stl', triangles)

# test_ds_stl()