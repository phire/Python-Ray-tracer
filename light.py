#from colour import Colour
from geom3 import *
import math

class Light(object):
    """A Basic light at inifinite distance"""

    def __init__(self, scene, dir, colour):
	self.colour = colour
	self.dir = dir
	self.scene = scene
	self.offset = 0.0000001 * self.dir

    def atPoint(self, point):
	shadowRay = Ray3(point + self.offset, self.dir)
	shadowTest = self.scene.intersect(shadowRay)
	if shadowTest is None:
	    return LightHit(self.colour, self.dir)
	return None

class LightHit(object):
    def __init__(self, colour, vector):
	self.colour = colour
	self.vector = vector

class PointLight(object):
    def __init__(self, scene, point, colour):
	self.colour = colour
	self.point = point
	self.scene = scene
	self.offset = 0.0000001

    def atPoint(self, point):
	dir = unit(self.point - point)
	shadowRay = Ray3(point + self.offset * dir, dir)
	shadowTest = self.scene.intersect(shadowRay)
	if shadowTest is None or shadowTest.entry > length(self.point - point):
	    return LightHit(self.colour, dir)
	return None

class SpotLight(object):
    def __init__(self, scene, point, lookAt, angle, colour):
	self.colour = colour
	self.point = point
	self.vector = unit(point - lookAt)
	self.angle = math.cos(math.radians(angle))
	self.scene = scene
	self.offset = 0.0000001

    def atPoint(self, point):
	dir = unit(self.point - point)
	angle = abs(dot(dir, self.vector))
	#print angle
	if angle < self.angle:
	    return None
	shadowRay = Ray3(point + self.offset * dir, dir)
	shadowTest = self.scene.intersect(shadowRay)
	if shadowTest is None or shadowTest.entry > length(self.point - point):
	    return LightHit(self.colour, dir)
	return None


