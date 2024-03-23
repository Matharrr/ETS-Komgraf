from Bentuk_Bidang.ellips import draw_ellipse
from Bentuk_Bidang.lingkaran import draw_circle

class Telur:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.telur = draw_ellipse(x, y, 5, 7)
        self.embrio = draw_circle(x, y, 2)