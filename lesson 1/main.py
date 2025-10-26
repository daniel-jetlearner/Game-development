import pgzrun


WIDTH = 1000
HEIGHT = 1000

wood = Actor("wood")
wood.pos = (300,700)
orange = Actor("orange")
orange.pos = (400,800)
plane = Actor("plane")
plane.pos = (300,500)
alien = Actor("alien")
alien.pos = (100,700)
def draw():
    screen.fill("dark blue")
    alien.draw()
    plane.draw()
    orange.draw()
    wood.draw()


def update():
    pass

pgzrun.go()