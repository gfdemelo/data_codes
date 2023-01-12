#!/usr/bin/env python

import numpy as np
from scipy.special import jn
import pylab

# Vertical range of the diffraction pattern: plot nlayer line layers above and
# below the centre horizontal 
nlayers = 5
ymin, ymax = -nlayers, nlayers

# Horizontal range of the diffraction pattern, x = 2pi.r.R
xmin, xmax = -10, 10
npts = 4000
x = np.linspace(xmin, xmax, npts)

# Diffraction pattern along each line layer: |Jn(x)|^2
# for n = 0, 1, ..., nlayers-1
layers = np.array([jn(i, x)**2 for i in range(nlayers)])

# Obtain the indexes of the maxima in each layer
maxi = [(np.diff(np.sign(np.diff(layers[i,:]))) < 0).nonzero()[0] + 1
                                                    for i in range(nlayers)]

# Create the SVG image, using circles of different radii for diffraction spots
svg_name='eg8-dna-diffraction.svg'
canvas_width = canvas_height = 500
fo = open(svg_name, 'w')
print("""<?xml version="1.0" encoding="utf-8"?>
         <svg xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink"
              width="{}" height="{}" style="background: {}">""".format(
                canvas_width, canvas_height, '#ffffff'), file=fo)

def svg_circle(r, cx, cy):
    """ Return the SVG mark up for a circle of radius r centred at (cx,cy). """
    return r'<circle r="{}" cx="{}" cy="{}"/>'.format(r, cx, cy)

# For each spot in each layer, draw a circle on the canvas. The circle radius
# is the scaled value of the diffraction intensity maximum, with a ceiling
# value of spot_max_radius because the centre spots are very intense
spot_scaling, spot_max_radius = 50, 20
for i in range(nlayers):
    for j in maxi[i]:
        sx = (x[j] - xmin)/(xmax-xmin) * canvas_width
        sy = (i - ymin)/(ymax - ymin) * canvas_height
        spot_radius = min(layers[i,j]*spot_scaling, spot_max_radius)
        print(svg_circle(spot_radius, sx, sy), file=fo)
        if i:
            # The pattern is symmetric about the centre horizontal:
            # duplicate the layers with i > 0
            sy = canvas_height - sy
            print(svg_circle(spot_radius, sx, sy), file=fo)

print(r'</svg>', file=fo)

