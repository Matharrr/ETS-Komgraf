import numpy as np
import py5

# ubah menjadi class
class Lingkaran:
    def __init__(self, xc, yc, radius):
        self.xc = xc
        self.yc = yc
        self.radius = radius
        self.points = self.lingkaran(xc, yc, radius)
        
    def circlePlotPoints(self, x, y):
        res = [
            [self.xc + x, self.yc + y],
            [self.xc - x, self.yc + y],
            [self.xc + x, self.yc - y],
            [self.xc - x, self.yc - y],
            [self.xc + y, self.yc + x],
            [self.xc - y, self.yc + x],
            [self.xc + y, self.yc - x],
            [self.xc - y, self.yc - x],
            ]
        return res

    def lingkaran(self, xc, yc, radius):
        x = 0
        y = radius
        p = 1 - radius
        res = self.circlePlotPoints(x, y) 
        while(x < y):
            x+=1
            if (p < 0):
                p+= 2*x + 1
            else:
                y-=1
                p+= 2*(x-y) + 1
            
            res = np.concatenate(
                (
                    res
                    , self.circlePlotPoints(x, y)
                ), axis=0)
        return res

    def draw(self):
        for point in self.points:
            py5.point(*point)