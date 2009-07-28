"""A ray-traceable Plane is a Plane through a given
   point with a given normal and surface material.
   It needs an intersect method that returns the
   point of intersection of a given ray with the
   plane and a normal method that returns the normal
   at a given point (which is irrelevant for a plane
   as the normal is the same everywhere)."""

from geom3 import Vector3, Point3, Ray3, dot, unit
from math import sqrt

class Plane(object):
    """A ray-traceable plane"""
    
    def __init__(self, point, normal, material):
        """Create a plane through a given point with given normal
        and surface material"""
        self.point = point
        self.Pnormal = normal
        self.material = material


    def normal(self, p):
        """The surface normal at the given point"""
        # Normal is always the same for a plane
        return self.Pnormal


    def intersect(self, ray):
        """The ray t value of the first intersection point of the
        ray with self, or None if no intersection occurs"""
        t = dot((self.point - ray.start), self.Pnormal/(dot(ray.dir, self.Pnormal)))
        if t < 0:
            return None
        return t

    def texCords(self, point):
    	vect = point - self.point
	u = vect.dx
	v = vect.dz
	return (u, v)
    	

    

