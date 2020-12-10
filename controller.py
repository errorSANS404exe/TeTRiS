import pygame
from pygame import event

import model

TIMER = event.custom_type()
pygame.time.set_timer(TIMER, 300)


# (1000)


def event_processing():
    # контроллер
    e = event.get()
    for among_us in e:
        if among_us.type == TIMER:
            model.move_block()
        if among_us.type == pygame.QUIT:
            exit()
