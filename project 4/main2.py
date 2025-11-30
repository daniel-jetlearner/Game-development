import random
import pgzrun


WIDTH = 500
HEIGHT = 500



flower = []


for i in range(10):
    flw = Actor("flower")
    flw.pos = random.randint(50,450), random.randint(50,450)
    flower.append(flw)




def draw():
    screen.blit("background",(0,0))
    for f in flower:
        f.draw()



















pgzrun.go()