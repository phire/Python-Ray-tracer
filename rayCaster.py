import cProfile
from geom3 import Point3, Vector3, Ray3, cross, dot, unit, length
from math import sqrt, tan
from colour import Colour
from sphere import Sphere
from plane import Plane
import Image
from material import Material
from scene import Scene
from light import Light
from texture import *


# Define various scene constants

WIN_SIZE = 400                              # Screen window size (square)
SPACING = 1.0 / WIN_SIZE                    # Pixel spacing on viewplane

SHINY_RED = Material(Colour(0.7, 0.1, 0.2), Colour(0.4,0.4,0.4), 100, 0.2)
SHINY_BLUE = Material(Colour(0.2, 0.3, 0.7), Colour(0.8,0.8,0.8), 200, 0.3)
MATT_GREEN = Material(None, None, None, 0.3, Texture_Check(6, Colour(0,0,0), Colour(0.5,0.5,0.5)))

EYEPOINT = Point3(0.5, 0.5, 2)

SCENE = Scene([Sphere(Point3(0.35,0.6,0.5), 0.25, SHINY_BLUE),
               Sphere(Point3(0.75,0.2,0.6), 0.15, SHINY_RED),
               Plane(Point3(0,0,0), Vector3(0,1,0), MATT_GREEN)])

lights = [Light(SCENE, unit(Vector3(2,5,3)), Colour(0.8, 0.8, 0.8)),
	  Light(SCENE, unit(Vector3(-4,5,0)), Colour(0.3, 0.3, 0.3))]
SCENE.background = Colour(0, 0, 0)
SCENE.ambient = Colour(0.1, 0.1, 0.1) 

class rayCaster(object):
    def __init__(self):
	return

    def rayColour(self, ray, depth=0):
	if depth > 100:
	    print "Max Depth reached!"
	    return Colour(0,0,0)
	
        hitPoint = SCENE.intersect(ray)
        if hitPoint is None:
            return SCENE.background
        else:
            (obj, t) = hitPoint
            surface = obj.material
	    point = ray.pos(t)
            normal = obj.normal(point)
            view = -ray.dir
	    colour = Colour(0,0,0)
	    
	    # Reflective ray
	    if surface.reflectivity:
		r = -2 * ray.dir.dot(normal) * normal + ray.dir
		Rray = Ray3(point + r * 0.0000001, r)
		colour += surface.reflectivity * self.rayColour(Rray, depth+1)

	    texCords = None
	    if surface.texture:
		texCords = obj.texCords(point)

	    # Surface Colour
            return colour + surface.litColour(normal, SCENE.ambient, 
	    	map(lambda x: x.atPoint(point), lights), view, texCords)

    # Main body. Set up an image then compute colour at each pixel
    def trace(self):
        img = Image.new("RGB", (WIN_SIZE, WIN_SIZE))

        for row in range(WIN_SIZE):
            for col in range(WIN_SIZE):
                
                pixelCentre = Point3((col + 0.5) * SPACING, ((WIN_SIZE -row) + 0.5) * SPACING, 1)
                ray = Ray3(EYEPOINT, pixelCentre - EYEPOINT)

                img.putpixel((col, row), self.rayColour(ray).intColour())

        img.save("out.png")  # Display image in default image-viewer application

caster = rayCaster()
caster.trace()
