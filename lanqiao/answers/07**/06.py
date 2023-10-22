# 1、画12个菱形
# 2、画红色圆

import turtle as t
t.hideturtle()
def ling():
  t.fillcolor("yellow")
  t.begin_fill()
  for i in range(2):
      t.forward(80)
      t.right(60)
      t.forward(80)
      t.right(120)
  t.end_fill()

for i in range(12):
    t.penup()
    t.forward(120)
    t.pendown()
    t.left(30)
    ling()
    t.right(30)
    t.penup()
    t.forward(-120)
    t.pendown()
    t.right(360/12)

t.penup()
t.right(90)
t.forward(120)
t.left(90)
t.pendown()
t.pencolor("red")
t.circle(120,360)
t.done()
