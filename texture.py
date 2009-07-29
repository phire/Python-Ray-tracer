class Texture_Check(object):
    def __init__(self, size, c1, c2):
	self.colour1 = c1
	self.colour2 = c2
	self.size = size

    def colour(self, cords):
	(u, v) = cords
	u = u * self.size
	v = v * self.size
	if u < 0:
	    u = u - 1
	if v < 0:
	    v = v - 1
	if(int(u) % 2 != int(v) % 2):
	    return self.colour1
	return self.colour2
