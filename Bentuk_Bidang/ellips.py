import numpy as np
import py5

class Ellips:
    def __init__(self, xc, yc, a, b):
        self.xc = xc
        self.yc = yc
        self.a = a
        self.b = b
        self.points = self.ellipse(xc, yc, a, b)
        
    def ellipsePlotPoints(self, x, y):
        res = [
            [self.xc + x, self.yc + y],
            [self.xc - x, self.yc + y],
            [self.xc + x, self.yc - y],
            [self.xc - x, self.yc - y],
            ]
        return res

    def ellipse(self, xc, yc, a, b):
        x = 0
        y = b
        p = b**2 + a**2 * (1 - b) / 4
        res = self.ellipsePlotPoints(x, y) 
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
                    , self.ellipsePlotPoints(x, y)
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
                    , self.ellipsePlotPoints(x, y)
                ), axis=0)
        return res

    def draw(self):
        for point in self.points:
            py5.point(*point)