import pgzrun
import random

WIDTH = 600
HIGHT = 600


pacman = Actor("pacman")
dot = Actor("dot")
pacman.pos = (300,300)

dot.pos = random.randint(50,550), random.randint(50,550)

score = 0
def draw():
    screen.blit("background",(0,0))
    pacman.draw()
    dot.draw()
    screen.draw.text(f"score:{score}", color = "white",center=(500,20))

def on_mouse_down(pos):
    if dot.collidepoint(pos):
        dot.pos = random.randint(50,550), random.randint(50,550)


def update():
    global score

    if keyboard.d:
        pacman.x+=3

    if keyboard.a:
        pacman.x-=3

    if keyboard.w:
        pacman.y-=3

    if keyboard.s:
        pacman.y+=3


    if pacman.colliderect(dot):
        score+=10000
        dot.pos = random.randint(50,550), random.randint(50,550)








pgzrun.go()

