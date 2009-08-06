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
	if other.entry:
	    if other.entry > self.entry:
		self.entry = other.entry
		self.mat = other.mat
		self.normal = other.normal
		self.texCords = other.texCords
	if other.exit:
	    if self.exit:
		self.exit = min(self.exit, other.exit)
	    else:
		self.exit = other.exit
	return self
    
    def miss(self):
	return (self.exit < 0 and self.exit != None) or (self.exit != None and self.entry != None and (self.entry - self.exit) > 0.00000001)

