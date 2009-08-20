from geom3 import Point3, Vector3, unit
from colour import Colour
from sphere import Sphere
from plane import Plane
from material import Material
from scene import Scene
from light import *
from texture import *
from CSG import *
from camera import Camera

WIN_SIZE = 300                              # Screen window size (square)

SHINY_RED = Material(Colour(0.7, 0.1, 0.2), Colour(0.4,0.4,0.4), 100, .2)
SHINY_BLUE = Material(Colour(0.2, 0.3, 0.7), Colour(0.8,0.8,0.8), 200, .3)
MATT_GREEN = Material(Colour(0.1,0.85, 0.1))
CHECK_FLOOR = Material(None, None, None, None, Texture_Check(6, Colour(0,0,0), Colour(0.5,0.5,0.5)))

scene = Scene([
	       Sphere(Point3(0.35,0.6,0.5), 0.25, SHINY_BLUE),
	       #Difference([
	       Intersection([ # Cube
		  #Plane(Point3(0.2,0.0,0.5), Vector3(0,-1,0), CHECK_FLOOR),
		  Plane(Point3(0.1,0.175,0.8), Vector3(0.5, 1,0.1), SHINY_BLUE),
		  #Plane(Point3(0.1,0.1,0.5), Vector3(-1,0,0), CHECK_FLOOR),
		  #Plane(Point3(0.4,0.1,0.5), Vector3( 1,0,0), CHECK_FLOOR),
		  #Plane(Point3(0.5,0.1,0.8), Vector3(0,0, 1), CHECK_FLOOR),
		  #Plane(Point3(0.5,0.1,0.5), Vector3(0,0,-1), CHECK_FLOOR),
		  Sphere(Point3(0.1,0.175,0.8), 0.175, SHINY_BLUE),
			  ]),
		 #Sphere(Point3(0.1,0.175,0.8), 0.165, SHINY_BLUE)]),
	       #Sphere(Point3(0.75,0.15,.2), 0.15, SHINY_RED),
               Plane(Point3(0,0,0), Vector3(0,1,0), CHECK_FLOOR)
	       ])

scene.lights = [
	  #Light(scene, unit(Vector3(2,5,3)), Colour(0.6, 0.6, 0.6)),
	  #Light(scene, unit(Vector3(-4,3,0)), Colour(0.7, 0.7, 0.7)),
	  PointLight(scene, Point3(.5, 1.1, 1.2), Colour(0.9, 0.9, 0.9)),
	  ]
scene.background = Colour(0, 0, 0)
scene.ambient = Colour(0.4, 0.4, 0.4) 


camera = Camera(scene, Point3(0.5, 0.2, 1.6),WIN_SIZE)
camera.lookAt(Point3(0.5,0.2,0.3))
#camera.lookAt(Point3(0.1,0.1, 0.9))


