import pgzrun
import random


WIDTH = 500
HIGHT = 500

bee = Actor("bee")
flw = Actor("flower")
bee.pos=(250,250)

flw.pos = random.randint(50,450), random.randint(50,450)

score = 0
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flw.draw()
    screen.draw.text(f"score:{score}",color = "white",center= (400,20))

def on_mouse_down(pos):
    if flw.collidepoint(pos):
        flw.pos = random.randint(50,450), random.randint(50,450)







def update():
    global score


    if keyboard.right:
        bee.x+=3

    if keyboard.left:
        bee.x-=3
    
    if keyboard.up:
        bee.y-=3

    if keyboard.down:
        bee.y+=3

    if bee.colliderect(flw):
        score+=100
        flw.pos = random.randint(50,450), random.randint(50,450)
        
    








pgzrun.go()