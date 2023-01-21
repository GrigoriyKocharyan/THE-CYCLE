from pygame import *
from math import *
from random import *


import texts as t
import os

# ПЕРЕМЕННЫЕ \/
click = 0
scene = 0


# СПИСКИ \/
particles = []


class Particle:
    def __init__(self, win):
        self.win = win
    def draw(self):
        draw.circle(self.win, (10, 10, 10), (randint(0, 900), randint(0, 600)), randint(5, 20))



init()
win = display.set_mode((900, 600))

for i in range(100):
    particles.append(Particle(win))


while True:

    win.fill((0,0,0))

    m0 = mouse.get_pos()[0]
    m1 = mouse.get_pos()[1]

    w0 = win.get_size()[0]
    w1 = win.get_size()[1]

    for events in event.get():
        if events.type == QUIT:
            quit()
            exit()
        if events.type == MOUSEBUTTONDOWN:
            if BUTTON_LEFT:
                click = 1
        if events.type == MOUSEBUTTONUP:
            click = 0


    if scene == 0:

        for particle in particles:
            particle.draw()



        win.blit(t.THE_CYCLE, (w0/2 - t.THE_CYCLE.get_size()[0]/2, 100))

        draw.rect(win, (30,30,30), (w0/2 - 150, 300, 300, 60), 0, 20)


        win.blit(t.PLAY, (w0 / 2 - t.PLAY.get_size()[0] / 2, 305))

        pass
    if scene == 1:
        pass
    if scene == 2:
        pass
    if scene == 3:
        pass
    if scene == 4:
        pass



    display.flip()