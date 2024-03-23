import numpy as np
import math

def translate2D(tx, ty, tm):
    identity = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    return np.matmul(identity, tm)
def scale2D(sx, sy, refx, refy, tm):
    m = np.identity(3)
    m[0][0] = sx
    m[1][1] = sy
    m[0][2] = (1-sx)*refx
    m[1][2] = (1-sy)*refy
    return np.matmul(m, tm)

def rotate2D(a, refx, refy):
    m = np.array([
        [math.cos(math.radians(a)), -math.sin(math.radians(a)), refx *
         (1-math.cos(math.radians(a))) + refy*math.sin(math.radians(a))],
        [math.sin(math.radians(a)), math.cos(math.radians(a)), refy *
         (1-math.cos(math.radians(a))) - refx*math.sin(math.radians(a))],
        [0, 0, 1]
    ])
    return m

def transformPoints2D(pts, tm):
    i, _  = pts.shape
    
    for k in range(i):
        tmp = tm[0][0] * pts[k,0] + tm[0][1] * pts[k,1] + tm[0][2]
        pts[k,1] = tm[1][0] * pts[k,0] + tm[1][1] * pts[k,1] + tm[1][2]
        pts[k,0] = tmp

    return pts

def shear2D(shx, shy, refx, refy, tm):
    m = np.identity(3)
    m[0][1] = shx
    m[1][0] = shy
    m[0][2] = -shx * refy
    m[1][2] = -shy * refx
    return np.matmul(m, tm)