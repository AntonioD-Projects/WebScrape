#
#           ~~~ Graphics Tutorial ~~~
#

import math

import graphics
from graphics import *

import time

#import fun_practice
#from fun_practice import*
#-------------------------------------------------
# Step 1) Initialize window for computer graphics

win_width = 300
win_height = 200

window = GraphWin('Cool Name of Window', win_width, win_height)



def makePoly(p, n, r):
  #p = center Point
  #n = number of vertices
  #r = radius
  list_of_points = []
  for i in range(n):
    
    a = 360/n * i
    print(a)
    a = a * math.pi/180
    x = r*math.cos(a) + p[0]
    y = r*math.sin(a) + p[1]
    pnt = Point(x,y)
    list_of_points.append(pnt)
  poly = Polygon(list_of_points)
  return poly

p_c = [win_width//2, win_height//2]
nv = 4
rad = 20 
print('hello')
poly = makePoly(p_c, nv, rad)
poly.draw(window)

window.getMouse()
window.close()
