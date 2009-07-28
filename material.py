from geom3 import dot, unit

class Material(object):
    """A Material is something that can be illuminated by lighting
    to yield a colour. It is assumed that the ambient colour of the
    material is the same as its diffuse colour and there is no
    self-emission."""
    
    def __init__(self, diffuseColour, specularColour = None, shininess = None, 
		    reflectivity = None):
        """Initialise the diffuse and specular reflectances plus the
        specular highlight exponent.  specularColour and shininess are
        both None for a purely diffuse surface"""
        self.diffuseColour = diffuseColour
        self.specularColour = specularColour
        self.shininess = shininess
	self.reflectivity = reflectivity


    def litColour(self, normal, ambientLight, lights, viewVector):
        """The RGB colour of this material with the given surface
        normal under the given lighting when viewed from an
        eyepoint in the viewVector direction."""

	colour = ambientLight * self.diffuseColour
	
	for light in lights:
	    if light:
		if self.shininess:
		    H = unit(light.vector + viewVector)
		    colour += (max(0, normal.dot(light.vector)) * self.diffuseColour + 
			normal.dot(H)**self.shininess * self.specularColour) * light.colour
	        colour += max(0, normal.dot(light.vector)) * self.diffuseColour * light.colour

	return colour

        
