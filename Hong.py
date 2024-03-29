"""
First and Last Name:
Date:
COMP 313: Quiz 3
Quiz #:
Center Coordinates:
Rotation Degrees:
Axis of Rotation:
"""
import math
import random

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians #–or use numpy

import obj_to_rot_setup_quads
import obj_to_rot_setup_tris

# Point values for all vertices partitioned by axis
x = []
y = []
z = []

# New position in global coords
xg = []
yg = []
zg = []

vertex_count = 0

tri_shape_points = []

tri_shape_f = []

quad_shape_points = []

quad_shape_f = []

# based on selection, load data from .OBJ file into setup variables
def choose_solid_name(solid_name):
   global vertex_count, x, y, z, tri_shape_points, tri_shape_f, quad_shape_points, quad_shape_f
   if solid_name == 'tetrahedron' or solid_name == 'octahedron':
      vertex_count, x, y, z, tri_shape_points, tri_shape_f = \
         obj_to_rot_setup_tris.importObj(solid_name)
   elif solid_name == 'cube' or solid_name == 'die':
      vertex_count, x, y, z, quad_shape_points, quad_shape_f = \
         obj_to_rot_setup_quads.importObj(solid_name)
   pass

#———————————————————–function definitions
def rotx(xc, yc, zc, xp, yp, zp, Rx):
   a = [xp, yp, zp]
   b = [1, 0, 0] #———————————-[cx11,cx12,cx13]
   xpp=np.inner(a,b) #—–scalar product of a,b=xp*cx11+yp*cx12+ zp*cx13
   b = [0, cos(Rx),-sin(Rx)] #—————[cx21,cx22,cx23]
   ypp=np.inner(a,b)
   b = [0,sin(Rx),cos(Rx)] #[cx31,cx32,cx33]
   zpp=np.inner(a,b)
   [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
   return[xg,yg,zg]

def roty(xc,yc,zc,xp,yp,zp,Ry):
   Ry = Ry * math.pi/180
   a=[xp,yp,zp]
   b=[cos(Ry),0,sin(Ry)] #——————–[cx11,cx12,cx13]
   xpp=np.inner(a, b)
   b=[0,1,0] #—————[cx21,cx22,cx23]
   ypp=np.inner(a,b) #——————–scalar product of a,b
   b=[-sin(Ry),0,cos(Ry)] #—————[cx31,cx32,cx33]
   zpp=np.inner(a,b)
   [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
   return[xg,yg,zg]

def rotz(xc,yc,zc,xp,yp,zp,Rz):
   a=[xp,yp,zp]
   b=[cos(Rz),-sin(Rz),0] #——————-[cx11,cx12,cx13]
   xpp=np.inner(a, b)
   b=[sin(Rz),cos(Rz),0] #—————[cx21,cx22,cx23]
   ypp=np.inner(a,b)
   b=[0,0,1] #—————[cx31,cx32,cx33]
   zpp=np.inner(a,b) #———————scalar product of a,b
   [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
   return[xg,yg,zg]


def rotate_shape(xc, yc, zc, angle, R_axis, solid_name):

   # called to load set up variables
   choose_solid_name(solid_name)

   '''DEBUG PRINTING TO CHECK VALUES
   print(vertex_count)
   print(x)
   print(y)
   print(z)
   print(quad_shape_points)
   print(quad_shape_f)
   print(tri_shape_points)
   print(tri_shape_f)'''


   # moves every vertex
   for i in range(vertex_count):
      # creates a list element for every vertex
      xg.append(i)
      yg.append(i)
      zg.append(i)
      # rotates each iterated vetex, depending on rotational axis
      if R_axis == 'Rx':
         [xg[i], yg[i], zg[i]] = rotx(xc, yc, zc, x[i], y[i], z[i], angle)
      elif R_axis == 'Ry':
         [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], angle)
      elif R_axis == 'Rz':
         [xg[i], yg[i], zg[i]] = rotz(xc, yc, zc, x[i], y[i], z[i], angle)

      # collects each vertex as a point vector into a list of point vectors
      # based on solid name
      if solid_name == 'cube' or solid_name == 'die':
         quad_shape_points[i] = [xg[i], yg[i], zg[i]]
      elif solid_name == 'tetrahedron' or solid_name == 'octahedron':
         tri_shape_points[i] = [xg[i], yg[i], zg[i]]

   # plot the solid based on new point vectors and face defintions
   # quad choice
   if solid_name == 'cube' or solid_name == 'die':
      obj_to_rot_setup_quads.plot_shape(quad_shape_points, quad_shape_f)
   # tri choice
   elif solid_name == 'tetrahedron' or solid_name == 'octahedron':
      obj_to_rot_setup_tris.plot_shape(tri_shape_points, tri_shape_f)

pass
'''def roll_die() :
   choose_solid_name('die')
   rots = [random.randint(0, 3) * 90, random.randint(0, 3) * 90, random.randint(0, 3) * 90]
   orders = ['RxRzRy', 'RyRxRz', 'RzRyRx', 'RxRyRz', 'RyRzRx', 'RzRxRy']
   first = orders[random.randint(0, 5)]
   xc = 0
   yc = -1
   zc = 0
   # moves every vertex
   for i in range(vertex_count):
         # creates a list element for every vertex
      xg.append(i)
      yg.append(i)
      zg.append(i)
      if first[0:2] == 'Rx':
         # rotates each iterated vetex, depending on rotational axis
         [xg[i], yg[i], zg[i]] = rotx(xc, yc, zc, x[i], y[i], z[i], rots[0])
      elif first[0:2] == 'Ry':
         [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], rots[0])
      elif first[0:2] == 'Rz':
         [xg[i], yg[i], zg[i]] = rotz(xc, yc, zc, x[i], y[i], z[i], rots[0])
   for i in range(vertex_count):
      # creates a list element for every vertex
      xg.append(i)
      yg.append(i)
      zg.append(i)
      # rotates each iterated vetex, depending on rotational axis
      if first[2:4] == 'Rx':
         [xg[i], yg[i], zg[i]] = rotx(xc, yc, zc, x[i], y[i], z[i], rots[1])
      elif first[2:4] == 'Ry':
         [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], rots[1])
      elif first[2:4] == 'Rz':
         [xg[i], yg[i], zg[i]] = rotz(xc, yc, zc, x[i], y[i], z[i], rots[1])
   quad_shape_points[i] = [xg[i], yg[i], zg[i]]
   obj_to_rot_setup_quads.plot_shape(quad_shape_points, quad_shape_f)
   for i in range(vertex_count):
         # creates a list element for every vertex
      xg.append(i)
      yg.append(i)
      zg.append(i)
         # rotates each iterated vetex, depending on rotational axis
      if first[4:] == 'Rx':
         [xg[i], yg[i], zg[i]] = rotx(xc, yc, zc, x[i], y[i], z[i], rots[2])
      elif first[4:] == 'Ry':
         [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], rots[2])
      elif first[4:] == 'Rz':
         [xg[i], yg[i], zg[i]] = rotz(xc, yc, zc, x[i], y[i], z[i], rots[2])

      # collects each vertex as a point vector into a list of point vectors
      # based on solid name
   quad_shape_points[i] = [xg[i], yg[i], zg[i]]
   obj_to_rot_setup_quads.plot_shape(quad_shape_points, quad_shape_f)
   print(first)
   print(first[0:2]+'='+str(rots[0])+', '+first[2:4]+'='+str(rots[1])+', '+first[4:]+'='+str(rots[2
                                                                                      ]))

'''

def rotate_shape(xc, yc, zc, angle, R_axis, solid_name):

   # called to load set up variables
   choose_solid_name(solid_name)

   ''' DEBUG PRINTING TO CHECK VALUES
   print(vertex_count)
   print(x)
   print(y)
   print(z)
   print(quad_shape_points)
   print(quad_shape_f)
   print(tri_shape_points)
   print(tri_shape_f)
   '''

   # moves every vertex
   for i in range(vertex_count):
      # creates a list element for every vertex
      xg.append(i)
      yg.append(i)
      zg.append(i)
      # rotates each iterated vetex, depending on rotational axis
      if R_axis == 'Rx':
         [xg[i], yg[i], zg[i]] = rotx(xc, yc, zc, x[i], y[i], z[i], angle)
      elif R_axis == 'Ry':
         [xg[i], yg[i], zg[i]] = roty(xc, yc, zc, x[i], y[i], z[i], angle)
      elif R_axis == 'Rz':
         [xg[i], yg[i], zg[i]] = rotz(xc, yc, zc, x[i], y[i], z[i], angle)

      # collects each vertex as a point vector into a list of point vectors
      # based on solid name
      if solid_name == 'cube' or solid_name == 'die':
         quad_shape_points[i] = [xg[i], yg[i], zg[i]]
      elif solid_name == 'tetrahedron' or solid_name == 'octahedron':
         tri_shape_points[i] = [xg[i], yg[i], zg[i]]

   # plot the solid based on new point vectors and face defintions
   # quad choice
   if solid_name == 'cube' or solid_name == 'die':
      obj_to_rot_setup_quads.plot_shape(quad_shape_points, quad_shape_f)
   # tri choice
   elif solid_name == 'tetrahedron' or solid_name == 'octahedron':
      obj_to_rot_setup_tris.plot_shape(tri_shape_points, tri_shape_f)

pass


# User input method call
rotate_shape(0,0,0, 0, 'Ry', 'die')
