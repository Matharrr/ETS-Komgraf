from Bentuk_Bidang.ellips import draw_ellipse
from Bentuk_Bidang.segitiga_sama_kaki import segitiga_sama_kaki
from primitif.transformasi import rotate2D, transformPoints2D

class Kecebong:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.badan = draw_ellipse(x, y, 30, 12)
        self.mata1 = draw_ellipse(x+18, y-5, 3, 3)
        self.mata2 = draw_ellipse(x+18, y+5, 3, 3)
        self.ekor = segitiga_sama_kaki(x-30, y, 8, 20)
        
        self.ekor = transformPoints2D(x-30, y, 8, 20, rotate2D(90, x-30, y))