from geom3 import Vector3, Point3, Ray3, dot, unit
from hit import Hit

class Intersection(object):
    def __init__(self, objects):
	self.objs = objects

    def intersect(self, ray):
	hit = Hit(self, None, None)
	for o in self.objs:
	    hit = hit.intersection(o.intersect(ray))
	    if hit.miss(): 
	        if self.objs.index(o) != 0:
	            self.objs.remove(o)
		    self.objs = [o] + self.objs
		return None
	if hit.entry < hit.exit and hit.entry > 0:
	    return hit
	return None

