from Bentuk_Bidang.bentuk_dasar import BentukDasar
from primitif.basic import segitiga_sama_kaki

class SegitigaSamaKaki(BentukDasar):
    def __init__(self, x, y, alas, tinggi, tm=None):
        super().__init__(x, y, tm)
        self.alas = alas
        self.tinggi = tinggi
    
    def draw(self):
        super().draw(
            segitiga_sama_kaki(self.x, self.y, self.alas, self.tinggi),
        )