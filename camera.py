import math
from geom3 import *
import Image


class Camera(object):
    def __init__(self, scene, eyePoint, size):
	self.eyePoint = eyePoint
	self.size = size
	self.fov = 45
	self.viewUp = Vector3(0,1,0)
	self.at = Point3(.5,.5,.5)
	self.scene = scene

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

    def pixelColour(self, x, y):
        ray = self.getRay(x, y);
	# full scene anti alising goes here
	hit = self.processRay(ray)
	
	colour = hit.colour().intColour()
	self.img.putpixel((x, y), colour)
        return colour

