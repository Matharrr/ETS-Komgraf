from Bentuk_Bidang.ellips import draw_ellipse
from Bentuk_Bidang.segitiga_sama_kaki import segitiga_sama_kaki

class Kecebong:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.badan = draw_ellipse(x, y, 30, 12)
        self.mata1 = draw_ellipse(x+18, y-5, 3, 3)
        self.mata2 = draw_ellipse(x+18, y+5, 3, 3)
        self.ekor = segitiga_sama_kaki(x-30, y, 8, 20)
        # ini gmn anyg, biar si ekornya rotasi