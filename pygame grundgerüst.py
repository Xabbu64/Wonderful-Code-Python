import pygame as pg

class Element(pg.sprite.Sprite):
  def __init__(self, id, typ, image, pos, enable):
    super().__init__()
    self.id = id
    self.typ = typ
    self.image_e = pg.image.load(image='_e.png')
    self.image_d = pg.image.load(image='_d.png')
    self.enable = enable
    self.image = self.image_e.copy() if enable else self.image_d.copy()
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    self.selektiert = False

pg.init()
fenster_b, fenster_h = 1280,720
fenster = pg.display.set_mode((fenster_b, fenster_h))
zentrum = (fenster_b / 2, fenster_h / 2)
pfad = 'Wuerfelspiel/'
bild_gui = pg.image.load(f'{pfad}gui.png')
wuerfel_e = [pg.image.load(f'{pfad}{n+1}_e.png') for n in range(6)]
wuerfel_d = [pg.image.load(f'{pfad}{n+1}_d.png') for n in range(6)]
clock = pg.time.Clock()
FPS = 60

#Zeichenschleife mit FPS Bildern pro Sekunde
while True:
  clock.tick(FPS)
  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT: quit()
  fenster.blit(bild_gui, (0,0))
  #fenster.fill('#000000') # Schwarzer Bildschirm
  
  pg.display.flip()