from Bentuk_Bidang.bentuk_dasar import BentukDasar
from primitif.basic import ellipse

class Ellips(BentukDasar):
    def __init__(self, x, y, rx, ry, tm=None):
        super().__init__(x, y, tm)
        self.rx = rx
        self.ry = ry

    def draw(self):
        super().draw(
            ellipse(self.x, self.y, self.rx, self.ry)
        )