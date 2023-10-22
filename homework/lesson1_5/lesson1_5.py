# homework 1 answer
print("*",end="")
print("*",end="")
print("*")
print("*",end="")
print("*",end="")
print("*")
print("*",end="")
print("*",end="")
print("*")

# homework 2 answer
a=5
b=10
t=a
a=b
b=t
print(a,b)

# homework 3 answer
n=int(input())
price1=3.0
price2=5.0
saving=(price1+price2)*n*0.2
print(format(saving,".2f"))

# homework 4 answer
import turtle
import turtle as t
t.pendown()     #下笔
t.forward(50)   #直行50
t.left(135)     # 左135
t.forward(71)   # 直行71
t.penup()       # 起笔
t.left(135)     # 左135
t.forward(50)   # 直行50回到起点
t.left(180)     # 掉头 left 180
t.pendown()
t.forward(150)  # 直行150
t.left(30)      # 转向30
t.forward(100)  # 直行100
t.left(120)     # 左转120
t.forward(100)  # 直行100
t.left(120)     # 左120
t.forward(100)  # 直行100
t.left(180)     # 转向180
t.penup()
t.forward(100)  # 直行100返回
t.left(90)      # 左90
t.pendown()
t.forward(150)  # 直150
t.right(90)
t.forward(50)
t.right(135)
t.forward(71)
t.right(135)
t.pendown()
t.forward(50)
t.left(90)
t.forward(100)
t.left(180)
t.penup()
t.forward(100)
t.left(120)
t.pendown()
t.forward(100)
t.left(120)
t.forward(100)

t.done()

# homework 5 answer
price=int(input())
num=int(input())
print("请付款",price*num,"元",sep="")

