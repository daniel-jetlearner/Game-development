import random
import pgzrun

WIDTH = 500
HEIGHT = 500


satellite = []


index = 1


for i in range(8):
    sat = Actor("satellite")
    sat.pos = random.randint(50,450), random.randint(50,450)
    satellite.append(sat)



def draw():
    screen.blit("background",(0,0))
    num = 1
    for s in satellite:
        s.draw()
        screen.draw.text(str(num),color = "white",pos = (s.x+5,s.y+10))
        num+=1

def on_mouse_down(pos):
    global index
    
    if satellite[index].collidepoint(pos):
        prev_sat.append[index-1] 


 
























pgzrun.go()