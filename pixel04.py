import pyxel
pyxel.init(120,120)
dir = 0
i = 0

def update():
  global dir,i
  if dir == 1:
    i -= 2  # 移動速度を倍にする
    if i <= 0:
      dir = 0

  if dir == 0:
      i += 2  # 移動速度を倍にする
      if i >= 120:
        dir = 1

def draw():
  global i
  pyxel.cls(0)
  pyxel.circ(i,60,5,12)
  
pyxel.run(update,draw)
