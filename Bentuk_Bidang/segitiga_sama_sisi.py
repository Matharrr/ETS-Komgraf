import primitif.line
import py5

def segitiga_sama_sisi(x, y, sisi):
    py5.points(primitif.line.line_dda(x, y, x+sisi, y))
    py5.points(primitif.line.line_dda(x+sisi, y, x, y+sisi))
    py5.points(primitif.line.line_dda(x, y+sisi, x, y))