from Bentuk_Bidang.bentuk_dasar import BentukDasar
from Bentuk_Bidang.ellips import Ellips
from Bentuk_Bidang.segitiga_sama_kaki import SegitigaSamaKaki

class Kecebong(BentukDasar):
    def __init__(self, x, y, tm=None):
        super().__init__(x, y, tm)
        self.badan = Ellips(x, y, 30, 12)
        self.mata1 = Ellips(x+18, y-5, 3, 3)
        self.mata2 = Ellips(x+18, y+5, 3, 3)
        self.ekor = SegitigaSamaKaki(x-30, y, 8, 20)
        
    def draw(self):
        super().draw(
            self.badan,
            self.mata1,
            self.mata2,
            self.ekor
        )