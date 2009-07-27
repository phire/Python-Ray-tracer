"""A ray-traceable sphere is a sphere with a given
   centre and radius and a given surface material.
   It needs an intersect method that returns the
   point of intersection of a given ray with the
   sphere and a normal method that returns the
   surface at a given point on the sphere surface."""

from geom3 import Vector3, Point3, Ray3, dot, unit
from math import sqrt

class Sphere(object):
    """A ray-traceable sphere"""
    
    def __init__(self, centre, radius, material):
        """Create a sphere with a given centre point, radius
        and surface material"""
        self.centre = centre
        self.radius = radius
        self.material = material


    def normal(self, p):
        """The surface normal at the given point on the sphere"""
        return unit(p - self.centre)


    def intersect(self, ray):
        """The ray t value of the first intersection point of the
        ray with self, or None if no intersection occurs"""
        t = None
        q = self.centre - ray.start
        vDotQ = dot(ray.dir, q)
        squareDiffs = dot(q, q) - self.radius*self.radius
        discrim = vDotQ * vDotQ - squareDiffs
        if discrim >= 0:
            root = sqrt(discrim)
            t0 = (vDotQ - root)
            t1 = (vDotQ + root)
            if t0 > 0:
                t = t0
            elif t1 > 0:
                t = t1
        return t
    

    def __repr__(self):
        return "Sphere(%s, %.3f)" % (str(self.centre), self.radius)

# Two simple sanity tests if module is run directly

if __name__ == "__main__":
    sphere = Sphere(Point3(1,0,0), 1, None)
    ray = Ray3(Point3(1,0,5), Vector3(0,0,-1))
    missingRay = Ray3(Point3(1,0,5), Vector3(0,0,1))
    assert abs(sphere.intersect(ray) - 4.0) < 0.00001
    assert sphere.intersect(missingRay) is None
