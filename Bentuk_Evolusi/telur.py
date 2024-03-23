from Bentuk_Bidang.bentuk_dasar import BentukDasar
from Bentuk_Bidang.ellips import Ellips
from Bentuk_Bidang.lingkaran import Lingkaran

class Telur(BentukDasar):
    def __init__(self, x, y, tm=None):
        super().__init__(x, y, tm)
        self.telur = Ellips(x, y, 5, 7)
        self.embrio = Lingkaran(x, y, 2)
        
    def draw(self):
        super().draw(
            self.telur,
            self.embrio
        )