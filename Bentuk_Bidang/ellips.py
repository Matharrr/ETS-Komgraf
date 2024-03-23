import numpy as np
import py5

def ellipsePlotPoints(xc, yc, x, y):
    res = [
        [xc + x, yc + y],
        [xc - x, yc + y],
        [xc + x, yc - y],
        [xc - x, yc - y],
        ]
    return res

def ellipse(xc, yc, a, b):
    x = 0
    y = b
    p = b**2 + a**2 * (1 - b) / 4
    res = ellipsePlotPoints(xc, yc, x, y) 
    while(b**2 * (x + 1) < a**2 * (y - 0.5)):
        x+=1
        if (p < 0):
            p+= b**2 * (2*x + 1)
        else:
            y-=1
            p+= b**2 * (2*x + 1) + a**2 * (-2*y + 1)
        
        res = np.concatenate(
            (
                res
                , ellipsePlotPoints(xc, yc, x, y)
            ), axis=0)
    p = b**2 * (x + 0.5)**2 + a**2 * (y - 1)**2 - a**2 * b**2
    while(y > 0):
        y-=1
        if (p > 0):
            p+= a**2 * (-2*y + 1)
        else:
            x+=1
            p+= b**2 * (2*x + 1) + a**2 * (-2*y + 1)
        
        res = np.concatenate(
            (
                res
                , ellipsePlotPoints(xc, yc, x, y)
            ), axis=0)
    return res

def draw_ellipse(xc, yc, a, b):
    points = ellipse(xc, yc, a, b)
    for point in points:
        py5.point(*point)