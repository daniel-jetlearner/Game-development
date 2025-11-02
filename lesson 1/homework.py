import pgzrun 



wood = Actor('wood')       
wood.pos = (150, 300)

plane = Actor('plane')     
plane.pos = (400, 300)

orange = Actor('orange')       
orange.pos = (650, 300)


def draw():
    screen.clear()
    screen.fill((0, 0, 30))  
    screen.draw.text("favorite dialogue!", (100, 50), color="white", fontsize=40)


    wood.draw()
    plane.draw()
    orange.draw()

   
    if dialogue:
        screen.draw.text(dialogue, center=(400, 500), color="yellow", fontsize=36)


def draw():
    screen.clear()
    screen.fill((0, 0, 30))  
    screen.draw.text("click and hear them", (100, 50), color="white", fontsize=40)

    tung.draw()
    trala.draw()
    odin.draw()

    if dialogue:
        screen.draw.text(dialogue, center=(400, 500), color="yellow", fontsize=36)

def on_mouse_down(pos):
    global dialogue
    if tung.collidepoint(pos):
        dialogue = "Tung Tung Tung Sahhur "
    elif trala.collidepoint(pos):
        dialogue = "bombbordillo"
    elif odin.collidepoint(pos):
        dialogue = "odin din din din dun"
    else:
        dialogue = "" 


pgzrun.go()
