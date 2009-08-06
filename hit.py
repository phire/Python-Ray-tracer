class Hit(object):
    def __init__(self, obj, entry, exit, normal=None, material=None, TexCords=None):
        self.obj = obj
    	self.entry = entry
	self.exit = exit
	self.normal = normal
	self.mat = material
	self.texCords = TexCords

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

