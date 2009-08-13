from geom3 import Ray3, dot, unit 


class Hit(object):
    def __init__(self, obj, ray, entry, exit, normal=None, material=None, TexCords=None):
        self.obj = obj
    	self.entry = entry
	self.exit = exit
	self.normal = normal
	self.mat = material
	self.texCords = TexCords
	self.ray = ray
	self.reflection = None
	self.bgcolour = None

    def __lt__(self, other):
    	return self.entry < other.entry

    def __gt__(self, other):
	return self.entry > other.entry

    def intersection(self, other):
	"""Returns the intersection of 2 hits"""
	ret = self
	if other is None :
	    return ret	    #fixme: Is this the best option?
	if other.entry:
	    if other.entry > self.entry:
		ret.entry = other.entry
		ret.mat = other.mat
		ret.normal = other.normal
		ret.texCords = other.texCords
	if other.exit:
	    if self.exit:
		ret.exit = min(self.exit, other.exit)
	    else:
		ret.exit = other.exit
	return ret

    def union(self, other):
	"""Returns the union of 2 hits"""
	ret = self
	if other is None :
	    return ret
	if other.entry:
	    if not (self.entry and self.entry < other.entry):
		ret.entry = other.entry
		ret.mat = other.mat
		ret.normal = other.normal
		ret.texCords = other.texCords
	if other.exit:
	    if other.exit > self.exit:
		ret.exit = other.exit
	return ret
    
    def difference(self, other):
	"""Returns the driffence of 2 hits"""
	ret = self
	if other is None :
	    return ret
	if other.exit:
	    if other.exit > self.entry and other.entry < self.entry:
		ret.entry = other.exit
		ret.mat = other.mat
		ret.normal = other.normal
		ret.texCords = other.texCords
	return ret
    
    def miss(self):
	return (self.exit < 0 and self.exit != None) or (self.exit != None and self.entry != None and (self.entry - self.exit) > 0.00000001)

    def calcLights(self, scene):
	"""Calculate lights for the hit.
	Note: Call this after calcReflections so reflections get lights too"""
	self.lights = [l.atPoint(self.ray.pos(self.entry)) for l in scene.lights]
	self.ambient = scene.ambient
	if self.reflection:
	    self.reflection.calcLights(scene) # recurse to reflections
    
    def calcReflections(self, scene, depth=0):
	if self.mat.reflectivity and depth < 100:
	    dir = self.ray.dir
	    norm = self.normal
	    Rdir = -2 * dir.dot(norm) * norm + dir
	    ray = Ray3(self.ray.pos(self.entry) + Rdir * 0.0000001, Rdir)
	    self.reflection = scene.intersect(ray)
	    if self.reflection is not None:
	        self.reflection.calcReflections(scene, depth+1)
	    else:
		self.bgcolour = scene.background

    def colour(self):
	colour = self.mat.litColour(self.normal, self.ambient, self.lights,
		    -self.ray.dir, self.texCords)
	if self.reflection:
	    colour += self.mat.reflectivity * self.reflection.colour() 
	elif self.bgcolour:
	    colour += self.mat.reflectivity * self.bgcolour
	return colour

