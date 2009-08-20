#!/usr/bin/python
import cProfile
from antiAlaising import *
import Image
import sys
import time
from Tkinter import Tk, Canvas, PhotoImage
from camera import Camera

sys.path.insert(0,"scenes/")

#import balls as definition
definition = __import__(sys.argv[1])

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

    # Main body. Set up an image then compute colour at each pixel
    def trace(self):
        camera = definition.camera
        camera.img = Image.new("RGB", (camera.size, camera.size))

	print "ScottTracer"
        print "\tTracing Rays...   0%",
        sys.stdout.flush()

        count = 0
	t0 = time.clock()
        max = float(WIN_SIZE**2)
        lastPercentage = 0
        for row in range(WIN_SIZE):
            ROW = []
            for col in range(WIN_SIZE):
                count += 1

                pixel = camera.pixelColour(col, row)
		camera.img.putpixel((col, row), pixel.intColour())
                ROW.append(pixel.intColour())
            percentage = (count / max * 100)
            self.putImageRow(row, ROW)
            if percentage - lastPercentage > .9:
                print "\b\b\b\b\b\b%4.0f%%" % percentage,
                sys.stdout.flush()
                lastPercentage = percentage
        print "\b\b\b\b\b\b Done (%f sec)" % (time.clock() - t0)

	print "\tAnti-alasing...   0%",
        sys.stdout.flush()
	t0 = time.clock()
        count = 0
        lastPercentage = 0
        for row in range(WIN_SIZE):
            ROW = []
	    self.putImageRow(row, [(255,255,255)] * WIN_SIZE)
            for col in range(WIN_SIZE):
                count += 1

                pixel = camera.aa(col, row)
		camera.img.putpixel((col, row), pixel)
                ROW.append(pixel)
            percentage = (count / max * 100)
            self.putImageRow(row, ROW)
            if percentage - lastPercentage > .9:
                print "\b\b\b\b\b\b%4.0f%%" % percentage,
                sys.stdout.flush()
                lastPercentage = percentage
        print "\b\b\b\b\b\b (%f sec)" % (time.clock() - t0)

	print camera.pixels

        camera.img.save(sys.argv[1] + ".png")  # Display image in default image-viewer application

caster = rayCaster()
#cProfile.run("caster.root.mainloop()")
caster.root.mainloop()
