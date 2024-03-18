import turtle
import random 
renkler = ["red","blue","magenta","yellow","pink"]
turtle.penup()
turtle.goto(random.randint(-200,200),200)
turtle.pendown()
for a in range(1,5):
   # print(renkler[a])
    # turtle.color(renkler[a])
    turtle.color(random.choice(renkler))
    turtle.forward(100)
    turtle.right(90)
    
input()