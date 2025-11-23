import random
import pgzrun

WIDTH = 500
HEIGHT = 500


satellite = []


for i in range(8):
    sat = Actor("satellite")
    sat.pos = random.randint(50,450), random.randint(50,450)
    satellite.append(sat)



def draw():
    screen.blit("background",(0,0))
    for s in satellite:
        s.draw()



 
























pgzrun.go()