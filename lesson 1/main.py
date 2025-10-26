import pgzrun


WIDTH = 1000
HEIGHT = 1000

# wood = Actor("wood")
# wood.pos = (300,700)
# orange = Actor("orange")
# orange.pos = (400,800)
# plane = Actor("plane")
# plane.pos = (300,500)
alien = Actor("alien")
alien.pos = (100,700)
message = ("")
def draw():
    screen.fill("dark blue")
    alien.draw()
    screen.draw.text(message,color = "white",center = (60,150),fontsize = 50)
    # plane.draw()
    # orange.draw()
    # wood.draw()

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message =("well done")
    else:
        message = ("your a faliure")


def update():
    pass

pgzrun.go()