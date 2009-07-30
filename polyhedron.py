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
    def __init__(self, mat):
	self.material = mat
	self.halfspaces = [
			   Halfspace(Point3(0.2,0.0,0.5), Vector3(0,-1,0)),
			   Halfspace(Point3(0.2,0.175,0.5), Vector3(0, 1,0)),
			   Halfspace(Point3(0.1,0.1,0.5), Vector3(-1,0,0)),
			   Halfspace(Point3(0.4,0.1,0.5), Vector3( 1,0,0)),
			   Halfspace(Point3(0.5,0.1,0.8), Vector3(0,0, 1)),
			   Halfspace(Point3(0.5,0.1,0.5), Vector3(0,0,-1))
			  ]

    def normal(self, point):
	return self.Hacknormal
	

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

