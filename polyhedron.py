from geom3 import Vector3, Point3, Ray3, dot, unit
from hit import Hit

class Halfspace(object):
    def __init__(self, point, normal):
	self.point = point
	self.normal = unit(normal)
    
    def intersect(self, ray):
	t = None
	angle = ray.dir.dot(self.normal)
	if angle != 0:
	    t = (self.point - ray.start).dot(self.normal)/angle
	return (t, angle)

class Polyhedron(object):
    def __init__(self, halfspaces):
	self.halfspaces = halfspaces

    def intersect(self, ray):
	hit = Hit(self, None, None)
	for h in self.halfspaces:
	    hit = hit.intersection(h.intersect(ray))
	    if hit.miss(): 
	        if self.halfspaces.index(h) != 0:
	            self.halfspaces.remove(h)
		    self.halfspaces = [h] + self.halfspaces
		return None
	if hit.entry < hit.exit and hit.entry > 0:
	    return hit
	return None

