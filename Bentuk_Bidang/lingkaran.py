from Bentuk_Bidang.bentuk_dasar import BentukDasar
from primitif.basic import lingkaran

class Lingkaran(BentukDasar):
    def __init__(self, x, y, r, tm=None):
        super().__init__(x, y, tm)
        self.r = r
    
    def draw(self):
        super().draw(
            lingkaran(self.x, self.y, self.r),
        )