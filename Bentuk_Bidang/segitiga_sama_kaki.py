import primitif.line
import py5

class SegitigaSamaKaki:
    def __init__(self, x, y, alas, tinggi):
        self.x = x
        self.y = y
        self.alas = alas
        self.tinggi = tinggi
        self.points = self.segitiga_sama_kaki(x, y, alas, tinggi)
        
    def segitiga_sama_kaki(self, x, y, alas, tinggi):
        res = primitif.line.line_dda(x, y, x+alas, y)
        res += primitif.line.line_dda(x+alas, y, x+alas/2, y+tinggi)
        res += primitif.line.line_dda(x+alas/2, y+tinggi, x, y)
        return res

    def draw(self):
        for point in self.points:
            py5.point(*point)