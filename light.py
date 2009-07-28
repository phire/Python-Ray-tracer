#from colour import Colour
from geom3 import Ray3, Vector3, Point3

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

