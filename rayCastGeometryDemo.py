"""Simple demo of geometry of ray casting.
Scene contains two spheres and a flat box. Rays are shown being
case from eye point through the centre points of each pixel.
The example ray, shown differently, hits the red sphere, so its pixel
would be coloured red."""

import visual as vis

MID_GREY = (0.5,0.5,0.5)
LIGHT_GREY = (0.7,0.7,0.7)
YELLOW = (0.7,0.7,0.1)
BLACK = (0,0,0)
PIXELS = 5              # num pixels across and down
SPACING = 1.0 / PIXELS
SPECIAL_PIXEL = (3,1)   # Highlight this one

# Draw the viewplane grid

for t in vis.arange(0, 1.0001, SPACING):
    vis.curve(pos=[(0, t, 1), (1,t,1)], color = MID_GREY)
    vis.curve(pos=[(t,0,1), (t,1,1)], color = MID_GREY)

# Draw the eyepoint

eye = vis.vector(0.5, 0.5, 2)
#vis.label(pos=eye,text="Eye", xoffset=-10)
vis.sphere(pos=eye, color=BLACK, radius=0.02)

# Draw the scene

vis.sphere(pos=(0.35,0.6,0.5), radius=0.25, material=vis.materials.wood)
vis.sphere(pos=(0.75,0.2,0.6), radius=0.15, color=vis.color.red, material=vis.materials.plastic)
vis.box(pos=(0.5,0,0.5),height=0.001, color=vis.color.green)

# Draw a ray through each pixel centre

for x in range(PIXELS):
    for y in range(PIXELS):
        pixelCentre = vis.vector((x + 0.5) * SPACING, (y + 0.5) * SPACING, 1)
        vis.sphere(pos=pixelCentre, radius=0.01, color=vis.color.red)
        rayDir = pixelCentre - eye
        rayEnd = eye + 2 * rayDir   # Where ray hits z = 0 plane
        if (x,y) == SPECIAL_PIXEL:
            vis.curve(pos=[eye, rayEnd], color=(1,1,0), radius=0.004) 
        else:
            vis.curve(pos=[eye, rayEnd], color=LIGHT_GREY)       
        

vis.scene.autocenter = True
vis.scene.background = vis.color.white

          
