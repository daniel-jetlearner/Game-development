import random
import pgzrun

WIDTH = 500
HEIGHT = 500


satellite = []
start=[]
end=[]
gameover = False



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
    for i in range(len(start)):
        screen.draw.line(start[i],end[i], color = "yellow")


    if gameover:
        screen.draw.text("GAME OVER",pos = (125,250), color= "white", fontsize = 70)




def on_mouse_down(pos):
    global index
    
    if satellite[index].collidepoint(pos):
        prev_sat = satellite[index-1]
        curr_sat = satellite[index]
        start.append(prev_sat.pos)
        end.append(curr_sat.pos)
        index+=1 


def timefinish():
    global gameover

    start.clear()
    end.clear()
    satellite.clear()

    gameover = True



















clock.schedule(timefinish,2.0)
pgzrun.go()