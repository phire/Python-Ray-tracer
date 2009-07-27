from geom3 import dot, unit

class Material(object):
    """A Material is something that can be illuminated by lighting
    to yield a colour. It is assumed that the ambient colour of the
    material is the same as its diffuse colour and there is no
    self-emission."""
    
    def __init__(self, diffuseColour, specularColour = None, shininess = None):
        """Initialise the diffuse and specular reflectances plus the
        specular highlight exponent.  specularColour and shininess are
        both None for a purely diffuse surface"""
        self.diffuseColour = diffuseColour
        self.specularColour = specularColour
        self.shininess = shininess


    def litColour(self, normal, ambientLight, lightVector,
                  lightColour, viewVector):
        """The RGB colour of this material with the given surface
        normal under the given lighting when viewed from an
        eyepoint in the viewVector direction."""
        if lightColour is None:
            return ambientLight * self.diffuseColour
        if self.shininess:
            H = unit(lightVector + viewVector)
            return (self.diffuseColour * ambientLight + (max(0, normal.dot(lightVector)) * self.diffuseColour + normal.dot(H)**self.shininess * self.specularColour) * lightColour)
        return (self.diffuseColour * ambientLight + max(0, normal.dot(lightVector)) * self.diffuseColour * lightColour)

        
