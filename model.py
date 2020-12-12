import pygame

# ПОДГОТОВКА МОДЕЛИ
# создаем поле
pole_rect = pygame.Rect(300, 100, 300, 400)
pole_rect.centerx = 400

mesta=[1,0,0,1,0,1,1,0]


figura = []
block = pygame.Rect(300, 250, 50, 50)
figura.append(block)

block = pygame.Rect(300, 150, 50, 50)
figura.append(block)

block = pygame.Rect(300, 100, 50, 50)
figura.append(block)

block = pygame.Rect(300, 200, 50, 50)
figura.append(block)

schet = 0


def move_block():
    b = figura[0]
    print(b.bottom)
    if b.bottom >= pole_rect.bottom:
        return
    for wert in figura:
        wert.y += 5
