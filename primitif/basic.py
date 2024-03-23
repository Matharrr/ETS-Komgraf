import numpy as np
import py5
import primitif.line

def round(x):
    return int(x+0.5)

def draw_margin(width, height, margin, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin, margin, width-margin, margin))
    py5.points(primitif.line.line_dda(
        margin, height-margin, width-margin, height-margin))
    py5.points(primitif.line.line_bresenham(
        margin, margin, margin, height-margin))
    py5.points(primitif.line.line_bresenham(
        width-margin, margin, width-margin, height-margin))

def draw_grid(width, height, margin, c=[0, 0, 0, 255]):
    # Sumbu Y
    xa = margin
    ya = 2*margin
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)

    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa, ya, xb, ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa, ya, xa, yb))
        xa = xa + margin

def draw_kartesian(width, height, margin, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2, margin, width/2, height-margin))
    py5.points(primitif.line.line_bresenham(
        margin, height/2, width-margin, height/2))
    
def draw_bentuk(pts):
    py5.points(pts)
    
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

def segitiga_sama_kaki(x, y, alas, tinggi):
    py5.points(primitif.line.line_dda(x, y, x+alas, y))
    py5.points(primitif.line.line_dda(x+alas, y, x+alas/2, y+tinggi))
    py5.points(primitif.line.line_dda(x+alas/2, y+tinggi, x, y))

def segitiga_sama_sisi(x, y, sisi):
    py5.points(primitif.line.line_dda(x, y, x+sisi, y))
    py5.points(primitif.line.line_dda(x+sisi, y, x, y+sisi))
    py5.points(primitif.line.line_dda(x, y+sisi, x, y))