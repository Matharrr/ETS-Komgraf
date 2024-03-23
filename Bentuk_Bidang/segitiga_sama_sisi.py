import primitif.line
import py5

class SegitigaSamaSisi:
    def __init__(self, x, y, sisi):
        self.x = x
        self.y = y
        self.sisi = sisi
        self.points = self.segitiga_sama_sisi(x, y, sisi)
        
    def segitiga_sama_sisi(self, x, y, sisi):
        res = primitif.line.line_dda(x, y, x+sisi, y)
        res += primitif.line.line_dda(x+sisi, y, x, y+sisi)
        res += primitif.line.line_dda(x, y+sisi, x, y)
        return res

    def draw(self):
        for point in self.points:
            py5.point(*point)