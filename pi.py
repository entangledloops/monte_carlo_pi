# Author:      Stephen Dunn
# Date:        8/16/13
# File:        pi.py
# Description: Monte-Carlo Pi Estimator
# Notes:       exceeding ~pi to 4 decimal places with anything better than luck has low probability

import sys
import pygame
import math
import random

window = ""
width =  800
height = 600
resolution = 2000 # precision of line segments
points = 10000 # of points

def graph():
 
  x = y = ex = ey = 0
  dp = (math.pi/2)/resolution
  
  # draw a quarter-circle
  for i in range(0,resolution):
    x = ex
    y = ey
    ex = ex+dp
    ey = ey+dp

    pygame.draw.aaline(window, (128,255,128), \
        ( math.cos(x)*width, math.sin(y)*height ), \
        ( math.cos(ex)*width, math.sin(ey)*height ), 3)

  # estimate pi from random points
  hits = 0
  for i in range(0,points):
    px = random.random()
    py = random.random()
    c = math.sqrt( (px*px) + (py*py) ) 
    if (c <= 1.0): hits += 1
    px *= width
    py *= height
    pygame.draw.circle( window, (148,0,211), (int(px),int(py)), 1, 1 )

  api = 4.0*(float(hits)/float(points))
  font = pygame.font.SysFont('Arial', 18)
  pi_str = u'\u03c0' + ' ' + u'\u2248' + " " + "{0:.5f}".format(api)
  pi_str.encode('utf-8')
  print pi_str
  text = font.render(pi_str, True, (72,209,204))
  window.blit( text, (width/4,height/4) )
  
#----------------------------------
random.seed()
pygame.init()

window = pygame.display.set_mode( (width, height) )

print "graphing..."
graph()
print "done"

pygame.display.flip()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)
