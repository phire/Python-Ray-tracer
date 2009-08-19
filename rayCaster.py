#!/usr/bin/python
import cProfile
from antiAlaising import *
import Image
import sys
from Tkinter import Tk, Canvas, PhotoImage
from camera import Camera

sys.path.insert(0,"scenes/")

#import balls as definition
definition = __import__("balls")

WIN_SIZE = definition.camera.size

class rayCaster(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Ray Tracer")
        canvas = Canvas(self.root, width=WIN_SIZE , height=WIN_SIZE )
        self.image = PhotoImage(master=self.root, width=WIN_SIZE, height=WIN_SIZE)
        imageCentre = (WIN_SIZE / 2 + 2, WIN_SIZE / 2 + 2)
        canvas.create_image(imageCentre, image = self.image)
        canvas.pack()

        # Enqueue a callback to the ray tracer to start it going
        self.root.after(0, lambda : self.trace() )
        return

    def putImageRow(self, row, colours):
        """Output a list of colours to the specified row of the image.

        Tk uses horrible hexadecimal formatted colours, packed into
        a string separated by spaces and all enclosed in braces."
        """
        
        hexColours = ["#%02x%02x%02x" % colour for colour in colours]
        rowColourString = "{" + " ".join(hexColours) + "}"
        self.image.put(rowColourString, to=(0, row))
        self.root.update()

    def rayColour(self, ray, scene):
        
        hit = scene.intersect(ray)
        hit.calcReflections(scene)
        hit.calcLights(scene)
        return hit.colour()
            
    # Main body. Set up an image then compute colour at each pixel
    def trace(self):
        camera = definition.camera

        img = Image.new("RGB", (camera.size, camera.size))
        print "\tTracing Rays...   0%",
        sys.stdout.flush()

        count = 0
        max = float(WIN_SIZE**2)
        lastPercentage = 0
        for row in range(WIN_SIZE):
            ROW = []
            for col in range(WIN_SIZE):
                count += 1

                pixel = self.rayColour(camera.getRay(col, row), definition.scene)
                img.putpixel((col, row), pixel.intColour())
                ROW.append(pixel)
            percentage = (count / max * 100)
            self.putImageRow(row, [p.intColour() for p in ROW])
            if percentage - lastPercentage > .9:
                print "\b\b\b\b\b\b%4.0f%%" % percentage,
                sys.stdout.flush()
                lastPercentage = percentage
        print "\b\b\b\b\b\b Done"

        img.save("out.png")  # Display image in default image-viewer application

caster = rayCaster()
#cProfile.run("caster.root.mainloop()")
caster.root.mainloop()
