class NoAntiAliasing(object)
    def __init__(self, eyepoint, rayfunc)
    	self.eyepoint = eyepoint
	self.rayfunc = rayfunc
	
    def getPixel(self, pixelBox):
    	pixelCentre = Point3((col + 0.5) * SPACING, ((WIN_SIZE -row) + 0.5) * SPACING, 1)
