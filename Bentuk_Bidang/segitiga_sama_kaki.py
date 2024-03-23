import primitif.line
import py5

def segitiga_sama_kaki(x, y, alas, tinggi):
    py5.points(primitif.line.line_dda(x, y, x+alas, y))
    py5.points(primitif.line.line_dda(x+alas, y, x+alas/2, y+tinggi))
    py5.points(primitif.line.line_dda(x+alas/2, y+tinggi, x, y))
