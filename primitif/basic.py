import py5
import primitif.line

def round(x):
    return int(x+0.5)

def draw_margin(width, height, margin, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(margin, margin, width-margin, margin))
    py5.points(primitif.line.line_dda(
        margin, height-margin, width-margin, height-margin))
    py5.points(primitif.line.line_bresenham(
        margin, margin, margin, height-margin))
    py5.points(primitif.line.line_bresenham(
        width-margin, margin, width-margin, height-margin))

def draw_grid(width, height, margin, c=[0, 0, 0, 255]):
    # Sumbu Y
    xa = margin
    ya = 2*margin
    xb = width - xa
    yb = height - ya
    y_range = (height / margin)

    py5.stroke(c[0], c[1], c[2], c[3])
    for count in range(1, int(y_range)):
        py5.points(primitif.line.line_dda(xa, ya, xb, ya))
        ya = ya + margin

    # Sumbu X
    xa = 2*margin
    ya = margin
    xb = width - xa
    yb = height - ya
    x_range = (width / margin)
    for count in range(1, int(x_range)):
        py5.points(primitif.line.line_dda(xa, ya, xa, yb))
        xa = xa + margin

def draw_kartesian(width, height, margin, c=[0, 0, 0, 255]):
    py5.stroke(c[0], c[1], c[2], c[3])
    py5.points(primitif.line.line_dda(width/2, margin, width/2, height-margin))
    py5.points(primitif.line.line_bresenham(
        margin, height/2, width-margin, height/2))
    
def draw_bentuk(pts):
    py5.points(pts)