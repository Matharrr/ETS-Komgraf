import py5

from Bentuk_Evolusi.kecebong import Kecebong
from Bentuk_Evolusi.telur import Telur

egg = None
tadpole = None

def setup():
  global egg, tadpole
  py5.size(1000, 600)
  py5.background(255)
  

def draw():
  egg1 = Telur(130, 330)
  egg2 = Telur(140, 330)
  egg3 = Telur(150, 330)
  egg4 = Telur(160, 330)
  egg5 = Telur(135, 342)
  egg6 = Telur(145, 342)
  egg7 = Telur(155, 342)
  egg8 = Telur(140, 354)
  egg9 = Telur(140, 354)
  egg10 = Telur(150, 354)
  egg11 = Telur(160, 354)
  egg12 = Telur(145, 366)
  egg13 = Telur(155, 366)
  egg14 = Telur(150, 378)
  
  tadpole = Kecebong(310, 450)
    
def mouse_pressed():
  print(f'({py5.mouse_x}, {py5.mouse_y})')

if __name__ == '__main__':
  py5.run_sketch()