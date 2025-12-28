import pgzrun
import random



WIDTH = 800
HEIGHT = 500

ITEMS = ["batteryimg", "bagimg", "bottleimg", "chipsimg"]

level= 1

selected_items = []
selected_items_actor = []
animation = []



def setup():
    selected_items.clear()
    selected_items_actor.clear()
    for ani in animation:
        ani.stop()
    animation.clear()
    
    



    selected_items.append("paperimg")

    for i in range(level):
        item = random.choice(ITEMS)
        selected_items.append(item)

    random.shuffle(selected_items)

    gap=WIDTH/(level+2)
    x = gap
    for item in selected_items:
        actor = Actor(item)
        selected_items_actor.append(actor)
        actor.pos = x,50
        x+=gap

        ani = animate(actor, duration= 3, y = HEIGHT)
        animation.append(ani)



        


    
setup()
        
def draw():
    screen.blit("new_bg",  (0,0))
    for item in selected_items_actor:
        item.draw()




def on_mouse_down(pos):
    global level
    for i in range(level+1):
        item = selected_items_actor[i]
        if item.collidepoint(pos):
            if selected_items[i]== "paperimg":
                level+=1
                setup()
            
    




def update():
    pass

pgzrun.go()