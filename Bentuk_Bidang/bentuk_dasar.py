from primitif.basic import draw_bentuk
from primitif.transformasi import rotate2D, transformPoints2D, translate2D
from primitif.utility import convert_to_cartesian


class BentukDasar:
    def __init__(self, x, y, tm=None):
        self.x, self.y = convert_to_cartesian(x, y, 1000, 600, 0)
        self.tm = tm

    def draw(self, bidang):
        draw_bentuk(
            transformPoints2D(
                bidang,
                self.tm
            )
        )
        
    def move(self, x, y):
        self.tm = translate2D(x, y)
    
    def rotate(self, alpha, x=None, y=None):
        if alpha is None or alpha == 0:
            alpha = 90
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.tm = rotate2D(alpha, x, y, self.tm)