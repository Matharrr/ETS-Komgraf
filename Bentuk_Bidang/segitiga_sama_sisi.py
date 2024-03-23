from Bentuk_Bidang.bentuk_dasar import BentukDasar
from primitif.basic import segitiga_sama_kaki

class SegitigaSamaSisi(BentukDasar):
    def __init__(self, x, y, sisi, tm=None):
        super().__init__(x, y, tm)
        self.sisi = sisi
    
    def draw(self):
        super().draw(
            segitiga_sama_kaki(self.x, self.y, self.sisi, self.sisi),
        )