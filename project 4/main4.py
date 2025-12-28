import pgzrun




WIDTH = 500
HEIGHT = 500


rec = Actor("rectangle")
rec.pos = (400,400)
ball = Actor("ball")
ball.pos = (200,200)



score = 0
def draw():
    screen.blit("background",(0,0))

    rec.draw()
    ball.draw()
    screen.draw.text(f"score:{score}", color = "red",center=(250,20))






def update():
    global score

    if keyboard.d:
        rec.x+=3

    if keyboard.a:
        rec.x-=3






















pgzrun.go()