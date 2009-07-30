"""A scene is a list of objects. It provides an intersect
method to intersect a ray with the scene, returning the t
value (distance along the ray) at the first hit, plus
the object hit, in a pair. Written for COSC363.
@author Richard Lobb, June 22, 2009."""

class Scene(object):

    def __init__(self, objs = []):
        """Constructor takes a list of scene objects, each of which
        must provide an 'intersect' method that returns the ray t
        value or None of the first intersection between the ray and
        the object"""
        self.objs = objs


    def intersect(self, ray):
        """Intersect the given ray with all objects in the scene,
        returning the pair (obj, t) of the first hit or None if
        there are no hits"""

	mint = None
	mino = None
        for o in self.objs:
	    t = o.intersect(ray)
	    if t:
		if mino == None or  t < mint:
                    mint = t
		    mino = o
	if mint is not None:
	    return mino, mint
        return None

                
