import pgzrun
import random

score=0
game_over=False

TITLE="Bumble Bee Makes Flower Disappear!"
HEIGHT=500
WIDTH=600

bee=Actor("bee")
bee.pos=(100,100)

flower=Actor("flower")
flower.pos=(200,50)

def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))



pgzrun.go()