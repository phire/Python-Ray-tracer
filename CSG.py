from geom3 import Vector3, Point3, Ray3, dot, unit
from hit import Hit

class Intersection(object):
    def __init__(self, objects):
	self.objs = objects

    def intersect(self, ray):
	hit = Hit(self, ray, None, None)
	for o in self.objs:
	    hit = hit.intersection(o.intersect(ray))
	    if hit.miss(): 
	        #if self.objs.index(o) != 0:
	            #self.objs.remove(o)
		    #self.objs = [o] + self.objs
		return None
	return hit

class Union(object):
    def __init__(self, objects):
	self.objs = objects

    def intersect(self, ray):
	hit = Hit(self, ray, None, None)
	for o in self.objs:
	    hit = hit.union(o.intersect(ray))
	if hit.entry < hit.exit:
	    return hit
	return None

class Difference(object):
    def __init__(self, objects):
	self.objs = objects

    def intersect(self, ray):
	hit = self.objs[0].intersect(ray)
	if hit is not None:
	    hit = hit.difference(self.objs[1].intersect(ray))
	if hit and hit.entry < hit.exit:
	    return hit
	return None

