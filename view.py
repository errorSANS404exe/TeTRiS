from pygame import draw, display, font

import model, pygame

pygame.init()
print(font.get_fonts())
f = font.SysFont("comicsansms", 20, True)

size_of_block=model.pole_rect.width/8
def paint(okno):
    # вид
    okno.fill([200, 29, 90])
    draw.rect(okno, [0, 0, 0], model.pole_rect, 5)
    schet = f.render("0", True, [208, 147, 255])
    okno.blit(schet, [100, 100])
    for fruit in model.figura:
        draw.rect(color=[79, 240, 76], surface=okno, rect=fruit, width=3)
    # draw.rect(okno, [70, 199, 162], model.block)
    c = model.pole_rect.left
    for polus in model.mesta:
        b=pygame.Rect(c, 35, size_of_block,size_of_block)
        b.bottom=model.pole_rect.bottom
        draw.rect(okno, [234, 100, 24],b,2)
        c += size_of_block
    display.flip()
