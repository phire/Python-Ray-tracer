from geom3 import dot, unit
from colour import Colour

class Material(object):
    """A Material is something that can be illuminated by lighting
    to yield a colour. It is assumed that the ambient colour of the
    material is the same as its diffuse colour and there is no
    self-emission."""
    
    def __init__(self, diffuseColour, specularColour = None, shininess = None, 
		    reflectivity = None, texture = None):
        """Initialise the diffuse and specular reflectances plus the
        specular highlight exponent.  specularColour and shininess are
        both None for a purely diffuse surface"""
        self.diffuseColour = diffuseColour
        self.specularColour = specularColour
        self.shininess = shininess
	self.reflectivity = reflectivity
	self.texture = texture


    def litColour(self, normal, ambientLight, lights, viewVector, texCords):
        """The RGB colour of this material with the given surface
        normal under the given lighting when viewed from an
        eyepoint in the viewVector direction."""
	
	diffcol = self.diffuseColour
	if self.texture:
	    diffcol = check(texCords)
	
	colour = ambientLight * diffcol
	
	for light in filter(lambda x: x != None, lights) :
	    if self.shininess:
	        H = unit(light.vector + viewVector)
	        colour += (max(0, normal.dot(light.vector)) * diffcol + 
		    normal.dot(H)**self.shininess * self.specularColour) * light.colour
	    colour += max(0, normal.dot(light.vector)) * diffcol * light.colour

	return colour

def check(cords):
    (u, v) = cords
    u = u * 10
    v = v * 10
    if(int(u) % 2 != int(v) % 2):
	return Colour(0,0,0)
    return Colour(0.5,0.5,0.5)
