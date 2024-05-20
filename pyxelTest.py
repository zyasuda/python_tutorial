import pyxel
pyxel.init(120,120)
pyxel.cls(0)
for i in range(0,120,20):
  pyxel.line(0,0,120-i,i,5)
  for j in range(0,120,20):
    pyxel.circ(j,i,5,7)
pyxel.show()
