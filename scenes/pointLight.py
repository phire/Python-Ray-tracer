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

SHINY_RED = Material(Colour(0.7, 0.7, 0.7), Colour(0.4,0.4,0.4), 100, .2)
SHINY_SPHERE = Material(Colour(0.2, 0.3, 0.7), Colour(0.8,0.8,0.8), 200, .3)
MATT_CUBE = Material(Colour(0.7,0.7, 0.7), Colour(0.9,0.9,0.9), 300, .5)
MATT_PLANE = Material(Colour(0.6,0.6,0.6))

scene = Scene([
    Intersection([ # Cube
	Plane(Point3(0.5,0.0,0.5), Vector3(0,-1,0), MATT_CUBE),
	Plane(Point3(0.5,0.1,0.5), Vector3(0, 1,0), MATT_CUBE),
	Plane(Point3(0.2,0.0,0.5), Vector3(-1,.3,0), MATT_CUBE),
	Plane(Point3(0.8,0.0,0.5), Vector3( 1,.3,0), MATT_CUBE),
	Plane(Point3(0.5,0.0,0.8), Vector3(0,.3, 1), MATT_CUBE),
	Plane(Point3(0.5,0.0,0.2), Vector3(0,.3,-1), MATT_CUBE)]),
    Intersection([ # Cube
	Plane(Point3(0.5,0.0,0.5), Vector3(0,-1,0), MATT_CUBE),
	Plane(Point3(0.5,0.1,0.5), Vector3(0, 1,0), MATT_CUBE),
	Plane(Point3(0.2,0.0,0.5), Vector3(-1,.3,0), MATT_CUBE),
	Plane(Point3(0.8,0.0,0.5), Vector3( 1,.3,0), MATT_CUBE),
	Plane(Point3(0.5,0.0,0.8), Vector3(0,.3, 1), MATT_CUBE),
	Plane(Point3(0.5,0.0,0.2), Vector3(0,.3,-1), MATT_CUBE)]),
    Plane(Point3(0.5,0.0,0.0), Vector3(0,1,0) MATT_PLANE),
    Plane(Point3(0.5,0.0,-1), Vector3(0,0,1) MATT_PLANE),
])
 
scene.lights = [
        SpotLight(scene, Point3(-1, 1,  1.2), Point3(0.5,0.5,0.5), 25, Colour(0,0,1)),
]
scene.background = Colour(0, 0, 0)
scene.ambient = Colour(0.3, 0.3, 0.3) 


camera = Camera(scene, Point3(1.5, 0.9, 1.6),WIN_SIZE)
camera.lookAt(Point3(0.5,0.1,0.5))
camera.setFoV(30)


