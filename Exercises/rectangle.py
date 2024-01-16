import time
import turtle
import random

color1 = random.randrange(0, 100)
color2 = random.randrange(0, 100)
color3 = random.randrange(0, 100)

T = turtle.Pen()
T.speed(600)
T.pencolor(color1, color2, color3)

for i in range(0, 10000):
    T.forward(i)
    T.left(91)


time.sleep(2)
