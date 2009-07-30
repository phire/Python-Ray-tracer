from geom3 import Vector3, Point3, Ray3, dot, unit

class Halfspace(object):
    def __init__(self, point, normal):
	self.point = point
	self.normal = unit(normal)
    
    def intersect(self, ray):
	t = None
	angle = unit(ray.dir).dot(self.normal)
	if angle != 0:
	    t = (self.point - ray.start).dot(self.normal)/angle
	return (t, angle)

class Polyhedron(object):
    def __init__(self, halfspaces, mat):
	self.material = mat
	self.halfspaces = halfspaces

    def normal(self, point):
	return self.Hacknormal # TODO: Do this without a hack, or make intersect return normals too
	

    def intersect(self, ray):
	entry = None
	exit = None
	for h in self.halfspaces:
	    (t, e) =  h.intersect(ray)
	    if e < 0:
		if t > entry:
		    entry = t
		    self.Hacknormal = h.normal
	    else:
		if exit:
		    exit = min(t, exit)
		else: exit = t
	#print "[", entry,",", exit, "]"
	if entry < exit and entry > 0:
	    return entry
	return None

