''' general utilities '''
import math, random

# def naive_dist2

def flatten(x):
	return [z for y in x for z in y]

def get_rand_coordinate():
	return [2*math.pi*random.random(), 2*math.pi*random.random()]

