import time, view, pygame, controller, model
from pygame import display

pygame.init()
okno = display.set_mode([800, 600])

while 1 == 1:
    controller.event_processing()
    view.paint(okno)
    time.sleep(1 / 60)
