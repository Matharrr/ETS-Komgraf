from Bentuk_Bidang.ellips import draw_ellipse


class KecebongBerkaki:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.badan = draw_ellipse(x+18, y, 30, 10)