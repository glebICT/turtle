@ -0,0 +1,15 @@
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

bob = turtle.Turtle()

bob.color(random.random(), random.random(), random.random())
for _ in range(3):
    bob.forward(100)
    bob.left(120) 
     

turtle.done()