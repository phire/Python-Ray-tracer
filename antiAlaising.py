from geom3 import Point3, Vector3, Ray3, cross, dot, unit, length

class NoAA(object):
    def __init__(self, eyepoint, rayfunc):
    	self.eyepoint = eyepoint
	self.rayfunc = rayfunc
	
    def getPixel(self, pixelBox):
	(x, y, x2, y2) = pixelBox
    	pixelCentre = Point3((x + x2)/2, (y2 + y)/2, 1)
	ray = Ray3(self.eyepoint, pixelCentre - self.eyepoint)
	return self.rayfunc(ray)

class SuperSampling(object):
    def __init__(self, eyepoint, rayfunc):
	self.eyepoint = eyepoint
	self.rayfunc = rayfunc

    def getPixel(self, pixelBox):
	(x, y, x2, y2) = pixelBox
	PixelCenters = [Point3((x + x2)/2 + , (y2 + y)/2, 1)


