import math
from geom3 import *
import Image
from colour import Colour


class Camera(object):
    def __init__(self, scene, eyePoint, size):
	self.eyePoint = eyePoint
	self.size = size
	self.fov = 45
	self.viewUp = Vector3(0,1,0)
	self.at = Point3(.5,.5,.5)
	self.scene = scene
	self.maxLength = 0
	self.pixels = [0,0,0,0,0,0,0,0,0]

	self.Update()

    def Update(self):
	self.n = unit(self.at - self.eyePoint)
	self.u = unit(cross(self.viewUp, self.n))
	self.v = cross(self.n, self.u)
	self.VPC = self.eyePoint - self.n
	self.Wp = (2 * math.tan(math.radians(self.fov) / 2)) / self.size

    def lookAt(self, point):
	"""Set the point to look at"""
	self.at = point
	self.Update()

    def setFoV(self, angle):
	"""Set the Feild of view"""
	self.fov = angle
	self.Update()

    def setUp(self, vector):
	self.viewUp = unit(vector)
	self.Update()

    def getPixelCenter(self, x, y):
	x = x - self.size/2
	y = y - self.size/2
	return self.VPC + x * self.Wp * self.u + y * self.Wp * self.v

    def getRay(self, x, y):
	return Ray3(self.eyePoint, self.eyePoint - self.getPixelCenter(x, y))

    def processRay(self, ray):
	hit = self.scene.intersect(ray)
	hit.calcReflections(self.scene)
        hit.calcLights(self.scene)
        return hit

    def pixelColour(self, x, y, samples=1):
	pitch = .5 / samples
	colour = Colour(0,0,0)
	count = 0
	for subX in range(samples):
	  for subY in range(samples):
	    count += 1
	    ray = self.getRay(x - .5 + (subX+1) * pitch + subX*pitch, 
			      y - .5 + (subY+1) * pitch + subY*pitch)
	    hit = self.processRay(ray)
	    colour = colour + hit.colour()
	    #depth = math.log((hit.length() + 0.1), 10)
	    #colour = colour + Colour(depth, depth, depth)

	self.pixels[samples] += 1 
        return colour / count

    def aa(self, x, y):
	"""Detect if the pixel x,y is at an edge, then anti-alais it"""

	#This code is ugly, I can't work out a more sane way to do it
	M = self.size -1
	(p1, p2, p3, p4, p6, p7, p8, p9) = [(0,0,0)] * 8
	if x > 1 and y > 1: p1 = self.img.getpixel((x-1, y-1))
	if y > 1: p2 = self.img.getpixel((x, y-1))
	if x < M and y > 1: p3 = self.img.getpixel((x+1, y-1))
	if x > 1: p4 = self.img.getpixel((x-1, y))
	p5 = self.img.getpixel((x, y))
	if x < M: p6 = self.img.getpixel((x+1, y))
	if x > 1 and y < M: p7 = self.img.getpixel((x-1, y+1))
	if y < M: p8 = self.img.getpixel((x, y+1))
	if x < M and y < M: p9 = self.img.getpixel((x+1, y+1))

	#print p1, p2, p3, p4, p5, p6, p7, p8, p9
	
	r = abs((p1[0] + 2 * p2[0] + p3[0]) - (p7[0] + 2 * p8[0] + p9[0])) + 	    abs((p2[0] + 2 * p6[0] + p9[0]) - (p1[0] + 2 * p4[0] + p7[0]))
	g = abs((p1[1] + 2 * p2[1] + p3[1]) - (p7[1] + 2 * p8[1] + p9[1])) + 	    abs((p2[1] + 2 * p6[1] + p9[1]) - (p1[1] + 2 * p4[1] + p7[1]))
	b = abs((p1[2] + 2 * p2[2] + p3[2]) - (p7[2] + 2 * p8[2] + p9[2])) + 	    abs( (p2[2] + 2 * p6[2] + p9[2]) - (p1[2] + 2 * p4[2] + p7[2]) )

	sum = r + g + b

	if sum > 1200: # We do 2 levels of AA
	    colour = self.pixelColour(x, y, 4) # 16 samples per pixel
	    return colour.intColour()
	elif sum > 900:
	    colour = self.pixelColour(x, y, 3) # 9 samples per pixel
	    return colour.intColour()
	elif sum > 200:
	    colour = self.pixelColour(x, y, 2) # 4 samples per pixel
	    return colour.intColour()
	return p5

