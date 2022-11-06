import pygame as pg
aufloesung = 1000
pg.init()
weitermachen = True
spalten = 5
abstand = aufloesung // spalten
radius = (abstand-20) // 2
screen = pg.display.set_mode([aufloesung, aufloesung])
while weitermachen:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            weitermachen = False
    screen.fill((0,0,0))
    pg.draw.circle(screen,(255,255,255),(100,100),50,3)  

    pg.display.flip()
pg.quit()
