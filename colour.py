# The Colour class, a class to represent an RGB colour
# supporting addition and multiplication operations.
# Subtraction and division aren't currently supported.
# Written for COSC 363.
# @author Richard Lobb
# @version June 2009.


def toInt(floatVal):
    """Support function: convert a colour component in the range 0 - 1
    to the range 0 .. 255."""
    return max(0, min(255, int(256.0 * floatVal)))



class Colour(object):
    """Represents an RGB triple of floats, usually in the range 0 - 1.
    Can be multiplied on the left by a scalar or multiplied by another colour (which
    is done componentwise)."""

    def __init__(self, r, g, b):
        """Initialiser, given either a single parameter that's a sequence of red,
        green and blue components or three scalar R, G and B values"""
        self.r = r
        self.g = g
        self.b = b


    def __mul__(self, other):
        """Multiplication operator for colour * colour"""
        return Colour(self.r * other.r, self.g * other.g, self.b * other.b)


    def __rmul__(self, factor):
        """Reverse multiplication operator supports scalar * colour"""
        return Colour(factor * self.r, factor * self.g, factor * self.b)


    def __add__(self, other):
        """Plus operator for two colours"""
        return Colour(self.r + other.r, self.g + other.g, self.b + other.b)


    def __iadd__(self, other):
        """+= operator for two colours. Componentwise addition to self."""
        self.r += other.r
        self.g += other.g
        self.b += other.b
        return self


    def intColour(self):
        """Return an RGB triple of self's RGB components, each multiplied
        by 256 and clamped to the range 0..255"""
        return (toInt(self.r), toInt(self.g), toInt(self.b))
 

    def __str__(self):
        """Implementation of the str function"""
        return "(%.2f,%.2f,%.2f)" % (self.r, self.g, self.b)


    def __repr__(self):
        """The string representation (e.g. for serialisation) of self"""
        return "Colour(%f,%f,%f)"  % (self.r, self.g, self.b)


# Demo code to run if this file is run directly rather than just being imported.

if __name__ == "__main__":
    colourA = Colour(0.5, 0.2, 0.5)
    print "colourA:", str(colourA)
    colourB = 0.5 * colourA
    print "colourB:", str(colourB)
    reflectance = Colour(1, 0.5, 0.2)
    print "reflectance:", str(reflectance)
    print "colourB * reflectance", reflectance * colourB
    colourA += colourB
    print "After adding in colourB, colourA is: ", str(colourA)
    print "In (0..255) ints, colour A is:", colourA.intColour()
