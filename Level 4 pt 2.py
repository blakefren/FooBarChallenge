"""
Carrotland
==========

The rabbits are free at last, free from that horrible zombie science experiment. They need a happy, safe home, where they can recover.

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first, you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of two integers representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. The three vertices will not be collinear.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) vertices = [[2, 3], [6, 9], [10, 160]]
Output:
    (int) 289

Inputs:
    (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
Output:
    (int) 1730960165
    
Notes
=====

-Use Pick's theorem: # of integer vertices inside a rectangle of sides j and k = (j-1)(k-1)
-4 cases:
  -2 sides are on rectange (1 added triangle)
  -1 side is on rectange (2 added triangles)
  -0 sides are on rectange, non obtuse triangle (3 added triangles)
  -0 sides are in rectange, obtuse triangle (3 added triangles, one added rectangle)
-http://stackoverflow.com/questions/1049409/how-many-integer-points-within-the-three-points-forming-a-triangle
"""



from math import sqrt
from fractions import gcd
def answer(vertices):
  x = [x[0] for x in vertices]
  y = [y[1] for y in vertices]
  
  #Calculate area of triangle; don't use Heron's formula, always fails test 5...
  area = 0.5 * abs(x[0]*(y[1]-y[2]) + x[1]*(y[2]-y[0]) + x[2]*(y[0]-y[1]))
  
  #Calculate number of points on circumference using greatest common divisor formula
  num_pts = float(gcd(abs(x[0]-x[1]),abs(y[0]-y[1]))+gcd(abs(x[1]-x[2]),abs(y[1]-y[2]))+gcd(abs(x[2]-x[0]),abs(y[2]-y[0])))
  
  #Calculate and return number of points using Pick's Theorem
  return(int(round(area+1-(num_pts/2))))