import pygame,os, random, time
from pygame import mixer
import psutil, pygame_gui
from pygame_gui.elements.ui_drop_down_menu import UIDropDownMenu
from pygame.locals import *
from pygame_gui.windows.ui_confirmation_dialog import UIConfirmationDialog

pygame.init()
mixer.init()
pygame.display.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Sunday's Craziness | Chart Editor v2.51 beta")

manager = pygame_gui.UIManager((1280,720), None, True, None, "en", None)
manager2 = pygame_gui.UIManager((1280,720), None, True, None, "en", None)

class Arrow(pygame.sprite.Sprite):
  def __init__(self, x:float, y:float, maxy:float, speed:float):
    self.image = pygame.image.load("img/ui/arrow.png").convert()
    self.x = x
    self.y = y
    self.starty = y
    self.maxy = maxy
    self.speed = speed
  def update(self):
    if self.y <= self.maxy:
      self.y = self.starty
    self.y -= self.speed
    screen.blit(self.image, (self.x, self.y))
  def draw(self):
    screen.blit(self.image, (self.x, self.y))
  def rotate(self, angle:float):
    pygame.transform.rotate(self.image, angle)
  def scale(self, scalex:float, scaley:float):
    pygame.transform.scale(self.image,(scalex, scaley))

class Lines(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(50):
      self.sprites.append(pygame.image.load("img/fx/lines/" + str(i + 1) + ".png").convert())
    for i in range(50):
      self.sprites[i].set_colorkey(pygame.Color(0,0,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2
    self.image = self.sprites[int(self.current_sprite) % 50]
  def die(self):
    self.kill()

class ColorWave(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(50):
      self.sprites.append(pygame.image.load("img/fx/colorwave/" + str(i + 1) + ".jpg").convert())
    for i in range(50):
      self.sprites[i].set_colorkey(pygame.Color(0,0,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 50]
  def die(self):
    self.kill()

class Fire(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(102):
      self.sprites.append(pygame.image.load("img/fx/fire/" + str(i + 1) + ".jpg").convert())
    for i in range(102):
      self.sprites[i].set_colorkey(pygame.Color(0,0,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 102]
  def die(self):
    self.kill()

class Glitch1(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(75):
      self.sprites.append(pygame.image.load("img/fx/glitch1/" + str(i + 1) + ".jpg").convert())
    for i in range(75):
      self.sprites[i].set_colorkey(pygame.Color(0,0,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 75]
  def die(self):
    self.kill()

class Glitch2(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(12):
      self.sprites.append(pygame.image.load("img/fx/glitch2/" + str(i + 1) + ".jpg").convert())
    for i in range(12):
      self.sprites[i].set_colorkey(pygame.Color(35,35,35))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 12]
  def die(self):
    self.kill()

class Glitch3(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(41):
      self.sprites.append(pygame.image.load("img/fx/glitch3/" + str(i + 1) + ".jpg").convert())
    for i in range(41):
      self.sprites[i].set_colorkey(pygame.Color(0,0,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 41]
  def die(self):
    self.kill()

class Lights(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(50):
      self.sprites.append(pygame.image.load("img/fx/lights/" + str(i + 1) + ".jpg").convert())
    for i in range(50):
      self.sprites[i].set_colorkey(pygame.Color(0,0,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 50]
  def die(self):
    self.kill()

class Particles(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(50):
      self.sprites.append(pygame.image.load("img/fx/particles/" + str(i + 1) + ".jpg").convert())
    for i in range(50):
      self.sprites[i].set_alpha(128)
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 50]
  def die(self):
    self.kill()

class Rain(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(80):
      self.sprites.append(pygame.image.load("img/fx/rain/" + str(i + 5) + ".jpg").convert())
    for i in range(80):
      self.sprites[i].set_colorkey(pygame.Color(0,255,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 80]
  def die(self):
    self.kill()

class Smoke(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(127):
      self.sprites.append(pygame.image.load("img/fx/smoke/" + str(i + 1) + ".jpg").convert())
    for i in range(127):
      self.sprites[i].set_colorkey(pygame.Color(0,0,0))
      self.sprites[i].set_alpha(128)
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 127]
  def die(self):
    self.kill()

class Vhs(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.sprites = []
    for i in range(50):
      self.sprites.append(pygame.image.load("img/fx/vhs/" + str(i + 1) + ".jpg").convert())
    for i in range(50):
      self.sprites[i].set_colorkey(pygame.Color(0,255,0))
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]

    self.rect = self.image.get_rect()
    self.rect.topleft = [pos_x, pos_y]

  def update(self):
    self.current_sprite += 0.2

    self.image = self.sprites[int(self.current_sprite) % 50]
  def die(self):
    self.kill()

class PlayLine(pygame.sprite.Sprite):
  def __init__(self, posx:float, posy:float):
    super().__init__()
    self.posx = posx
    self.posy = posy
    self.rect = pygame.Rect(self.posx, self.posy, 265, 20)
    self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
  def update(self):
    randomstr = str(random.randint(1,4))
    s = mixer.Sound("audio/sfx/keyClick/keyClick"+randomstr+".mp3")
    s.set_volume(1)
    if self.rect.y <= 0:
      self.rect.y = 720
      forward()
    self.rect.y -= int(songspeedinput.get_current_value()) * 4
    pygame.draw.rect(screen, (0, 255, 0), self.rect)
    if self.rect.colliderect(note1) and sections[current_section][0] == 1 and self.rdict[0] == False:
      s.play()
      self.rdict = [True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note2) and sections[current_section][1] == 1 and self.rdict[1] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note3) and sections[current_section][2] == 1 and self.rdict[2] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note4) and sections[current_section][3] == 1 and self.rdict[3] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note5) and sections[current_section][4] == 1 and self.rdict[4] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note6) and sections[current_section][5] == 1 and self.rdict[5] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note7) and sections[current_section][6] == 1 and self.rdict[6] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note8) and sections[current_section][7] == 1 and self.rdict[7] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note9) and sections[current_section][8] == 1 and self.rdict[8] == False:
      randomstr = str(random.randint(1,4))
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note10) and sections[current_section][9] == 1 and self.rdict[9] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note11) and sections[current_section][10] == 1 and self.rdict[10] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note12) and sections[current_section][11] == 1 and self.rdict[11] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note13) and sections[current_section][12] == 1 and self.rdict[12] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note14) and sections[current_section][13] == 1 and self.rdict[13] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note15) and sections[current_section][14] == 1 and self.rdict[14] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note16) and sections[current_section][15] == 1 and self.rdict[15] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note17) and sections[current_section][16] == 1 and self.rdict[16] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note18) and sections[current_section][17] == 1 and self.rdict[17] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note19) and sections[current_section][18] == 1 and self.rdict[18] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note20) and sections[current_section][19] == 1 and self.rdict[19] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note21) and sections[current_section][20] == 1 and self.rdict[20] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note22) and sections[current_section][21] == 1 and self.rdict[21] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note23) and sections[current_section][22] == 1 and self.rdict[22] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note24) and sections[current_section][23] == 1 and self.rdict[23] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note25) and sections[current_section][24] == 1 and self.rdict[24] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note26) and sections[current_section][25] == 1 and self.rdict[25] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note27) and sections[current_section][26] == 1 and self.rdict[26] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note28) and sections[current_section][27] == 1 and self.rdict[27] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note29) and sections[current_section][28] == 1 and self.rdict[28] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note30) and sections[current_section][29] == 1 and self.rdict[29] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note31) and sections[current_section][30] == 1 and self.rdict[30] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note32) and sections[current_section][31] == 1 and self.rdict[31] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note33) and sections[current_section][32] == 1 and self.rdict[32] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note34) and sections[current_section][33] == 1 and self.rdict[33] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note35) and sections[current_section][34] == 1 and self.rdict[34] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note36) and sections[current_section][35] == 1 and self.rdict[35] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note37) and sections[current_section][36] == 1 and self.rdict[36] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note38) and sections[current_section][37] == 1 and self.rdict[37] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note39) and sections[current_section][38] == 1 and self.rdict[38] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note40) and sections[current_section][39] == 1 and self.rdict[39] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note41) and sections[current_section][40] == 1 and self.rdict[40] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note42) and sections[current_section][41] == 1 and self.rdict[41] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note43) and sections[current_section][42] == 1 and self.rdict[42] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note44) and sections[current_section][43] == 1 and self.rdict[43] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note45) and sections[current_section][44] == 1 and self.rdict[44] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False]
    elif self.rect.colliderect(note46) and sections[current_section][45] == 1 and self.rdict[45] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False]
    elif self.rect.colliderect(note47) and sections[current_section][46] == 1 and self.rdict[46] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False]
    elif self.rect.colliderect(note48) and sections[current_section][47] == 1 and self.rdict[47] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False]
    elif self.rect.colliderect(note49) and sections[current_section][48] == 1 and self.rdict[48] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False]
    elif self.rect.colliderect(note50) and sections[current_section][49] == 1 and self.rdict[49] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False]
    elif self.rect.colliderect(note51) and sections[current_section][50] == 1 and self.rdict[50] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False]
    elif self.rect.colliderect(note52) and sections[current_section][51] == 1 and self.rdict[51] == False:
      s.play()
      self.rdict = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
                  False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True]
  def resetpos(self):
    self.rect.y = 720
    self.rect.x = 490

class Key():
  def __init__(self, x, y, color1, color2,key):
    self.x = x
    self.y = y
    self.color1 = color1
    self.color2 = color2
    self.colorog = color1
    self.key = key
    self.rect = pygame.Rect(self.x, self.y, 45 * 1.25, 40 * 1.25)
    self.clicked = False
    self.k = pygame.mouse.get_pressed()
  def draw(self):
    if self.rect.collidepoint(pygame.mouse.get_pos()):
      if self.k[0] == 1 and self.clicked == False:
        self.clicked = True
      if self.k[1] == 1 and self.clicked == True:
        self.clicked = False

    if self.clicked == True:
      pygame.draw.rect(screen,self.color2,self.rect)
    else:
      pygame.draw.rect(screen,self.color1,self.rect)

class Note():
  def __init__(self, x:float, y:float, type):
    self.x = x
    self.y = y
    self.type = type
    self.width = 45 * 1.25
    self.height = 40 * 1.25
    self.color = (255,255,255)
    if self.type == "Deadly":
      self.width = 45 * 1.25
      self.height = 45 * 1.25
      self.color = (100,0,0)
    elif self.type == "Strum":
      self.width = 20 * 1.25
      self.height = 40 * 1.25
      self.color = (255,255,255)
      self.x += 15
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
  
  def update(self):
    pygame.draw.rect(screen, self.color, self.rect)


pygame.font.init()
fontsmall = pygame.font.Font("fonts/debug.ttf", 16)

sections = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
current_section = 0

notetype_sections = [
  ["Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal"],
  ["Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal"]
]

def showdawindow():
   mixer.Sound("audio/sfx/pop.mp3").play()
   tutowindow = pygame_gui.windows.UIMessageWindow(rect=pygame.Rect(0,0, 500,500), html_message="Chart Editor Tutorial:<br>1. Song Name: Here you input the song name and the files name.<br><br>2. Note Type: Here you choose the note's notetype, <br>e.g. Normal which is the normal one, Deadly which is the red one that takes score and Strum which is the strum for the notes.<br><br>3. Save File - Click on this button to save your chart to the place you want.<br>Recomendation: In the charts folder of the game.<br><br>4. Forward button and backward button (also known as arrow buttons) - They make you able to make more sections of notes than just one.<br>By clicking one of them you will go one section forward or behind.<br><br>5. Effect - In game's definition: It's an overlay lasting the song's length.<br><br>How to implement the song into the game:<br><br>1. Copy one of the songs file and name it however you want,<br>for e.g: The song's name. After that open it and change the value songName to your song name<br>MAKE SURE THAT THE NAME IS IN QUOTES.<br><br>2. Add the song into assets/audio/songs and make sure it's an mp3 file.<br>If you aren't sure turn on file extensions in the explorer by<br>clicking display then show and file extensions on windows 11,<br>but on windows 10 it's much easier, because you have to only click<br>view then check the file extensions checkbox.<br><br>3. Make your chart and save it. The game should automaticly save it in the right folder.<br><br>4. Open the game and enjoy your song!<br><br>", manager=manager2, window_title="Tutorial", object_id="#tutowindow", always_on_top=True)

def loaddaboi():
  global effectdrop, sections
  chartstring = ""
  try:
    with open("fxsettings/" + songinput.get_text() + ".txt", "r") as f:
      oneline = f.readline()
      if oneline.lower() == "lines" or oneline.lower() == "line" or oneline.lower() == "anime lines" or oneline.lower() == "anime line":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Anime Lines", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "rain":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Rain", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "colorwave" or oneline.lower() == "color wave":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Color Wave", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "fire":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Fire", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "glitch1" or oneline.lower() == "glitch 1":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Glitch 1", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "glitch2" or oneline.lower() == "glitch 2":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Glitch 2", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "glitch3" or oneline.lower() == "glitch 3":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Glitch 3", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "lights":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Lights", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "particles":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Particles", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "smoke":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "Smoke", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      elif oneline.lower() == "vhs":
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "VHS", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
      else:
        effectdrop.kill()
        effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "None", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")
    with open("charts/" + songinput.get_text() + ".txt", "r") as f:
      songspeedinput.set_current_value(float(f.readline()))
      data = f.readlines()
      for y in range(len(data)):
        chartstring += y
    sthval = 1
    sthval2 = 0
    for line in chartstring:
      if sthval == 1:
        if line == "0   ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
        if line == " 0  ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
        if line == "  0 ":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == "   0":
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "00  ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
        if line == " 00 ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == "  00":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0  0":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0 0 ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == " 0 0":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == " 000":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "000 ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == "00 0":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0 00":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0000":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line.lower() == "x   ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
        if line.lower() == " x  ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
        if line.lower() == "  x ":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == "   x":
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line.lower() == "xx  ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
        if line.lower() == " xx ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == "  xx":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line.lower() == "x  x":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line.lower() == "x x ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == " x x":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line.lower() == " xxx":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line.lower() == "xxx ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == "xx x":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line.lower() == "x xx":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][2] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line.lower() == "xxxx":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line == "|   ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
        if line == " |  ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
        if line == "  | ":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
        if line == "   |":
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == "||  ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
        if line == " || ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
        if line == "  ||":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == "|  |":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == "| | ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
        if line == " | |":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == " |||":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == "||| ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
        if line == "|| |":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == "| ||":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][2] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == "||||":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Strum"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line.lower() == "0x  ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
        if line.lower() == "0x||":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line.lower() == "0x |":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line.lower() == "0x| ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Deadly"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
        if line.lower() == "0 x ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == "0|x ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == "0 x|":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == "0|x|":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Strum"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line.lower() == "0  x":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line == "0  |":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line == " 0  ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
        if line.lower() == " 0x ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Deadly"
        if line == " 0| ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Strum"
        if line.lower() == " 0 x":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Deadly"
        if line == " 0 |":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Strum"
        if line.lower() == "x0  ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Deadly"
        if line == "  0 ":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == "   0":
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "00  ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
        if line == " 00 ":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == "  00":
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0  0":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0 0 ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == " 0 0":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == " 000":
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "000 ":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
        if line == "00 0":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0 00":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
        if line == "0000":
          sections[sthval2][0] = 1
          notetype_sections[sthval2][0] = "Normal"
          sections[sthval2][1] = 1
          notetype_sections[sthval2][1] = "Normal"
          sections[sthval2][2] = 1
          notetype_sections[sthval2][2] = "Normal"
          sections[sthval2][3] = 1
          notetype_sections[sthval2][3] = "Normal"
      if sthval == 13:
        sections.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        sthval2 += 1
        sthval = 0
      sthval += 1
  except:
    pygame_gui.windows.UIMessageWindow(rect=pygame.Rect(0,0, 100,100), html_message="Enter valid song name", manager=manager2, window_title="Error", always_on_top=True)

def savedaboi():
  mixer.Sound("audio/sfx/pop.mp3").play()
  if os.path.exists("charts/" + songinput.get_text() + ".txt"):
    os.remove("charts/" + songinput.get_text() + ".txt")
  with open("charts/" + songinput.get_text() + ".txt", "a+") as f1:
    savestring = ""
    for i in sections:
      if i == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
        counter += 1
        continue
      saveline = ""
      counter = 0
      for i2 in i:
        if sections[sections.index(i)][i.index(i2)] == 1:
          if notetype_sections[sections.index(i)][i.index(i2)] == "Normal":
            saveline += "0"
          elif notetype_sections[sections.index(i)][i.index(i2)] == "Strum":
            saveline += "|"
          else:
            saveline += "x"
        else:
          saveline += " "
        if counter % 4 == 3:
          savestring += saveline + "\n"
          saveline = ""
        counter += 1
    f1.write(str(songspeedinput.get_current_value()) + "\n" + savestring)
  with open("fxsettings/" + songinput.get_text() + ".txt", "a+") as f2:
    f2.write(effectdrop.selected_option[0])

savestuff = []
clock = pygame.time.Clock()
savebtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(0,0,100,40), text="Save File", manager=manager, object_id="#savebtn", command=savedaboi)
loadbtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(0,40,100,40), text="Load", manager=manager, object_id="#loadbtn", command=loaddaboi)
songtext = fontsmall.render("Song: ", False, (255,255,255))
songinput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(60, 100, 200, 40), manager=manager, object_id="#songentry", initial_text = "Write song name here")
songspeedtext = fontsmall.render("Song Speed: ", False, (255,255,255))
songspeedinput = pygame_gui.elements.UIHorizontalSlider(pygame.Rect(110, 150, 200,40), 1, [1, 20], manager=manager)
notetext = fontsmall.render("Note type: ", False, (255,255,255))
notetypedrop = UIDropDownMenu(["Normal", "Deadly", "Strum"], "Normal", relative_rect=pygame.Rect(110, 200, 200, 40), manager=manager, object_id="#notedrop")
effecttext = fontsmall.render("Effect: ", False, (255,255,255))
effectdrop = UIDropDownMenu(["None", "Anime Lines", "Color Wave", "Glitch 1", "Glitch 2", "Glitch 3", "VHS", "Smoke", "Rain", "Fire", "Lights", "Particles"], "None", relative_rect=pygame.Rect(110, 250, 200, 40), manager=manager, object_id="#notedrop")

tutorialbtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(0,670,100,50), text="Tutorial", manager=manager, object_id="#tutobtn",command=showdawindow)

def forward():
  global current_section
  current_section+=1
  sections.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
  notetype_sections.append(["Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal","Normal"])

def backward():
  global current_section
  if current_section != 0:
    current_section-=1

forwardbtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1230,670,50,50), text=">", manager=manager, object_id="#forwbtn", command=forward)
backwardbtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1175,670,50,50), text="<", manager=manager, object_id="#backbtn", command=backward)

mouseClicked = False

cycledbefore1 = False
cycledbefore2 = False
cycledbefore3 = False
cycledbefore4 = False
cycledbefore5 = False
cycledbefore6 = False
cycledbefore7 = False
cycledbefore8 = False
cycledbefore9 = False
cycledbefore10 = False
cycledbefore11 = False
cycledbefore12 = False
cycledbefore13 = False
cycledbefore14 = False
cycledbefore15 = False
cycledbefore16 = False
cycledbefore17 = False
cycledbefore18 = False
cycledbefore19 = False
cycledbefore20 = False
cycledbefore21 = False
cycledbefore22 = False
cycledbefore23 = False
cycledbefore24 = False
cycledbefore25 = False
cycledbefore26 = False
cycledbefore27 = False
cycledbefore28 = False
cycledbefore29 = False
cycledbefore30 = False
cycledbefore31 = False
cycledbefore32 = False
cycledbefore33 = False
cycledbefore34 = False
cycledbefore35 = False
cycledbefore36 = False
cycledbefore37 = False
cycledbefore38 = False
cycledbefore39 = False
cycledbefore40 = False
cycledbefore41 = False
cycledbefore42 = False
cycledbefore43 = False
cycledbefore44 = False
cycledbefore45 = False
cycledbefore46 = False
cycledbefore47 = False
cycledbefore48 = False
cycledbefore49 = False
cycledbefore50 = False
cycledbefore51 = False
cycledbefore52 = False

def clicked1():
  global cycledbefore1
  if sections[current_section][0] == 0:
    sections[current_section][0] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][0] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore1 = False

def clicked2():
  global drawrect2, cycledbefore2
  if sections[current_section][1] == 0:
    sections[current_section][1] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][1] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore2 = False

def clicked3():
  global drawrect3, cycledbefore3
  if sections[current_section][2] == 0:
    sections[current_section][2] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][2] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore3 = False

def clicked4():
  global drawrect4,cycledbefore4
  if sections[current_section][3] == 0:
    sections[current_section][3] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][3] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore4 = False

def clicked5():
  global drawrect5, cycledbefore5
  if sections[current_section][4] == 0:
    sections[current_section][4] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][4] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore5 = False

def clicked6():
  global drawrect6, cycledbefore6
  if sections[current_section][5] == 0:
    sections[current_section][5] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][5] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore6 = False

def clicked7():
  global drawrect7, cycledbefore7
  if sections[current_section][6] == 0:
    sections[current_section][6] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][6] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore7 = False

def clicked8():
  global drawrect8, cycledbefore8
  if sections[current_section][7] == 0:
    sections[current_section][7] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][7] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore8 = False

def clicked9():
  global drawrect9, cycledbefore9
  if sections[current_section][8] == 0:
    sections[current_section][8] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][8] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore9 = False

def clicked10():
  global drawrect10, cycledbefore10
  if sections[current_section][9] == 0:
    sections[current_section][9] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][9] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore10 = False

def clicked11():
  global drawrect11, cycledbefore11
  if sections[current_section][10] == 0:
    sections[current_section][10] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][10] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore11 = False

def clicked12():
  global drawrect12, cycledbefore12
  if sections[current_section][11] == 0:
    sections[current_section][11] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][11] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore12 = False

def clicked13():
  global drawrect13, cycledbefore13
  if sections[current_section][12] == 0:
    sections[current_section][12] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][12] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore13 = False

def clicked14():
  global drawrect14, cycledbefore14
  if sections[current_section][13] == 0:
    sections[current_section][13] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][13] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore14 = False

def clicked15():
  global drawrect15, cycledbefore15
  if sections[current_section][14] == 0:
    sections[current_section][14] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][14] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore15 = False

def clicked16():
  global drawrect16, cycledbefore16
  if sections[current_section][15] == 0:
    sections[current_section][15] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][15] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore16 = False

def clicked17():
  global drawrect17, cycledbefore17
  if sections[current_section][16] == 0:
    sections[current_section][16] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][16] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore17 = False

def clicked18():
  global drawrect18, cycledbefore18
  if sections[current_section][17] == 0:
    sections[current_section][17] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][17] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore18 = False

def clicked19():
  global drawrect19, cycledbefore19
  if sections[current_section][18] == 0:
    sections[current_section][18] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][18] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore19 = False

def clicked20():
  global drawrect20, cycledbefore20
  if sections[current_section][19] == 0:
    sections[current_section][19] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][19] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore20 = False

def clicked21():
  global drawrect21, cycledbefore21
  if sections[current_section][20] == 0:
    sections[current_section][20] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()

  else:
    sections[current_section][20] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore21 = False

def clicked22():
  global drawrect22, cycledbefore22
  if sections[current_section][21] == 0:
    sections[current_section][21] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][21] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore22 = False

def clicked23():
  global drawrect23, cycledbefore23
  if sections[current_section][22] == 0:
    sections[current_section][22] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][22] = 0 
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore23 = False

def clicked24():
  global drawrect24, cycledbefore24
  if sections[current_section][23] == 0:
    sections[current_section][23] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][23] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore24 = False

def clicked25():
  global drawrect25, cycledbefore25
  if sections[current_section][24] == 0:
    sections[current_section][24] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][24] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore25 = False

def clicked26():
  global drawrect26, cycledbefore26
  if sections[current_section][25] == 0:
    sections[current_section][25] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][25] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore26 = False

def clicked27():
  global drawrect27, cycledbefore27
  if sections[current_section][26] == 0:
    sections[current_section][26] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][26] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore27 = False

def clicked28():
  global drawrect28, cycledbefore28
  if sections[current_section][27] == 0:
    sections[current_section][27] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][27] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore28 = False

def clicked29():
  global drawrect29, cycledbefore29
  if sections[current_section][28] == 0:
    sections[current_section][28] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][28] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore29 = False

def clicked30():
  global drawrect30, cycledbefore30
  if sections[current_section][29] == 0:
    sections[current_section][29] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][29] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore30 = False

def clicked31():
  global drawrect31, cycledbefore31
  if sections[current_section][30] == 0:
    sections[current_section][30] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][30] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore31 = False

def clicked32():
  global drawrect32, cycledbefore32
  if sections[current_section][31] == 0:
    sections[current_section][31] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][31] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore32 = False

def clicked33():
  global drawrect33, cycledbefore33
  if sections[current_section][32] == 0:
    sections[current_section][32] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][32] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore33 = False

def clicked34():
  global drawrect34, cycledbefore34
  if sections[current_section][33] == 0:
    sections[current_section][33] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][33] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore34 = False

def clicked35():
  global drawrect35, cycledbefore35
  if sections[current_section][34] == 0:
    sections[current_section][34] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][34] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore35 = False

def clicked36():
  global drawrect36, cycledbefore36
  if sections[current_section][35] == 0:
    sections[current_section][35] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][35] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore36 = False

def clicked37():
  global drawrect37, cycledbefore37
  if sections[current_section][36] == 0:
    sections[current_section][36] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][36] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore37 = False

def clicked38():
  global drawrect38, cycledbefore38
  if sections[current_section][37] == 0:
    sections[current_section][37] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][37] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore38 = False

def clicked39():
  global drawrect39, cycledbefore39
  if sections[current_section][38] == 0:
    sections[current_section][38] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][38] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore39 = False

def clicked40():
  global drawrect40, cycledbefore40
  if sections[current_section][39] == 0:
    sections[current_section][39] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][39] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore40 = False

def clicked41():
  global drawrect41, cycledbefore41
  if sections[current_section][40] == 0:
    sections[current_section][40] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][40] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore41 = False

def clicked42():
  global drawrect42, cycledbefore42
  if sections[current_section][41] == 0:
    sections[current_section][41] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][41] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore42 = False

def clicked43():
  global drawrect43, cycledbefore43
  if sections[current_section][42] == 0:
    sections[current_section][42] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][42] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore43 = False

def clicked44():
  global drawrect44, cycledbefore44
  if sections[current_section][43] == 0:
    sections[current_section][43] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][43] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore44 = False

def clicked45():
  global drawrect45, cycledbefore45
  if sections[current_section][44] == 0:
    sections[current_section][44] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][44] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore45 = False

def clicked46():
  global drawrect46, cycledbefore46
  if sections[current_section][45] == 0:
    sections[current_section][45] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][45] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore46 = False

def clicked47():
  global drawrect47, cycledbefore47
  if sections[current_section][46] == 0:
    sections[current_section][46] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][46] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore47 = False

def clicked48():
  global drawrect48, cycledbefore48
  if sections[current_section][47] == 0:
    sections[current_section][47] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][47] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore48 = False

def clicked49():
  global drawrect49, cycledbefore49
  if sections[current_section][48] == 0:
    sections[current_section][48] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][48] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore49 = False

def clicked50():
  global drawrect50, cycledbefore50
  if sections[current_section][49] == 0:
    sections[current_section][49] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][49] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore50 = False

def clicked51():
  global drawrect51, cycledbefore51
  if sections[current_section][50] == 0:
    sections[current_section][50] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][50] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore51 = False

def clicked52():
  global drawrect52, cycledbefore52
  if sections[current_section][51] == 0:
    sections[current_section][51] = 1
    mixer.Sound("audio/sfx/chartPlace.mp3").play()
  else:
    sections[current_section][51] = 0
    mixer.Sound("audio/sfx/chartErase.mp3").play()
    cycledbefore52 = False

testbutton1 = pygame_gui.elements.UIButton(pygame.Rect(490, 670, 45 * 1.25, 40 * 1.25), "", manager, command=clicked1)
testbutton2 = pygame_gui.elements.UIButton(pygame.Rect(560, 670, 45 * 1.25, 40 * 1.25), "", manager, command=clicked2)
testbutton3 = pygame_gui.elements.UIButton(pygame.Rect(630, 670, 45 * 1.25, 40 * 1.25), "", manager, command=clicked3)
testbutton4 = pygame_gui.elements.UIButton(pygame.Rect(700, 670, 45 * 1.25, 40 * 1.25), "", manager, command=clicked4)
testbutton5 = pygame_gui.elements.UIButton(pygame.Rect(490, 615, 45 * 1.25, 40 * 1.25), "", manager, command=clicked5)
testbutton6 = pygame_gui.elements.UIButton(pygame.Rect(560, 615, 45 * 1.25, 40 * 1.25), "", manager, command=clicked6)
testbutton7 = pygame_gui.elements.UIButton(pygame.Rect(630, 615, 45 * 1.25, 40 * 1.25), "", manager, command=clicked7)
testbutton8 = pygame_gui.elements.UIButton(pygame.Rect(700, 615, 45 * 1.25, 40 * 1.25), "", manager, command=clicked8)
testbutton9 = pygame_gui.elements.UIButton(pygame.Rect(490, 560, 45 * 1.25, 40 * 1.25), "", manager, command=clicked9)
testbutton10 = pygame_gui.elements.UIButton(pygame.Rect(560, 560, 45 * 1.25, 40 * 1.25), "", manager, command=clicked10)
testbutton11 = pygame_gui.elements.UIButton(pygame.Rect(630, 560, 45 * 1.25, 40 * 1.25), "", manager, command=clicked11)
testbutton12 = pygame_gui.elements.UIButton(pygame.Rect(700, 560, 45 * 1.25, 40 * 1.25), "", manager, command=clicked12)
testbutton13 = pygame_gui.elements.UIButton(pygame.Rect(490, 505, 45 * 1.25, 40 * 1.25), "", manager, command=clicked13)
testbutton14 = pygame_gui.elements.UIButton(pygame.Rect(560, 505, 45 * 1.25, 40 * 1.25), "", manager, command=clicked14)
testbutton15 = pygame_gui.elements.UIButton(pygame.Rect(630, 505, 45 * 1.25, 40 * 1.25), "", manager, command=clicked15)
testbutton16 = pygame_gui.elements.UIButton(pygame.Rect(700, 505, 45 * 1.25, 40 * 1.25), "", manager, command=clicked16)
testbutton17 = pygame_gui.elements.UIButton(pygame.Rect(490, 450, 45 * 1.25, 40 * 1.25), "", manager, command=clicked17)
testbutton18 = pygame_gui.elements.UIButton(pygame.Rect(560, 450, 45 * 1.25, 40 * 1.25), "", manager, command=clicked18)
testbutton19 = pygame_gui.elements.UIButton(pygame.Rect(630, 450, 45 * 1.25, 40 * 1.25), "", manager, command=clicked19)
testbutton20 = pygame_gui.elements.UIButton(pygame.Rect(700, 450, 45 * 1.25, 40 * 1.25), "", manager, command=clicked20)
testbutton21 = pygame_gui.elements.UIButton(pygame.Rect(490, 395, 45 * 1.25, 40 * 1.25), "", manager, command=clicked21)
testbutton22 = pygame_gui.elements.UIButton(pygame.Rect(560, 395, 45 * 1.25, 40 * 1.25), "", manager, command=clicked22)
testbutton23 = pygame_gui.elements.UIButton(pygame.Rect(630, 395, 45 * 1.25, 40 * 1.25), "", manager, command=clicked23)
testbutton24 = pygame_gui.elements.UIButton(pygame.Rect(700, 395, 45 * 1.25, 40 * 1.25), "", manager, command=clicked24)
testbutton25 = pygame_gui.elements.UIButton(pygame.Rect(490, 340, 45 * 1.25, 40 * 1.25), "", manager, command=clicked25)
testbutton26 = pygame_gui.elements.UIButton(pygame.Rect(560, 340, 45 * 1.25, 40 * 1.25), "", manager, command=clicked26)
testbutton27 = pygame_gui.elements.UIButton(pygame.Rect(630, 340, 45 * 1.25, 40 * 1.25), "", manager, command=clicked27)
testbutton28 = pygame_gui.elements.UIButton(pygame.Rect(700, 340, 45 * 1.25, 40 * 1.25), "", manager, command=clicked28)
testbutton29 = pygame_gui.elements.UIButton(pygame.Rect(490, 285, 45 * 1.25, 40 * 1.25), "", manager, command=clicked29)
testbutton30 = pygame_gui.elements.UIButton(pygame.Rect(560, 285, 45 * 1.25, 40 * 1.25), "", manager, command=clicked30)
testbutton31 = pygame_gui.elements.UIButton(pygame.Rect(630, 285, 45 * 1.25, 40 * 1.25), "", manager, command=clicked31)
testbutton32 = pygame_gui.elements.UIButton(pygame.Rect(700, 285, 45 * 1.25, 40 * 1.25), "", manager, command=clicked32)
testbutton33 = pygame_gui.elements.UIButton(pygame.Rect(490, 230, 45 * 1.25, 40 * 1.25), "", manager, command=clicked33)
testbutton34 = pygame_gui.elements.UIButton(pygame.Rect(560, 230, 45 * 1.25, 40 * 1.25), "", manager, command=clicked34)
testbutton35 = pygame_gui.elements.UIButton(pygame.Rect(630, 230, 45 * 1.25, 40 * 1.25), "", manager, command=clicked35)
testbutton36 = pygame_gui.elements.UIButton(pygame.Rect(700, 230, 45 * 1.25, 40 * 1.25), "", manager, command=clicked36)
testbutton37 = pygame_gui.elements.UIButton(pygame.Rect(490, 175, 45 * 1.25, 40 * 1.25), "", manager, command=clicked37)
testbutton38 = pygame_gui.elements.UIButton(pygame.Rect(560, 175, 45 * 1.25, 40 * 1.25), "", manager, command=clicked38)
testbutton39 = pygame_gui.elements.UIButton(pygame.Rect(630, 175, 45 * 1.25, 40 * 1.25), "", manager, command=clicked39)
testbutton40 = pygame_gui.elements.UIButton(pygame.Rect(700, 175, 45 * 1.25, 40 * 1.25), "", manager, command=clicked40)
testbutton41 = pygame_gui.elements.UIButton(pygame.Rect(490, 120, 45 * 1.25, 40 * 1.25), "", manager, command=clicked41)
testbutton42 = pygame_gui.elements.UIButton(pygame.Rect(560, 120, 45 * 1.25, 40 * 1.25), "", manager, command=clicked42)
testbutton43 = pygame_gui.elements.UIButton(pygame.Rect(630, 120, 45 * 1.25, 40 * 1.25), "", manager, command=clicked43)
testbutton44 = pygame_gui.elements.UIButton(pygame.Rect(700, 120, 45 * 1.25, 40 * 1.25), "", manager, command=clicked44)
testbutton45 = pygame_gui.elements.UIButton(pygame.Rect(490, 65, 45 * 1.25, 40 * 1.25), "", manager, command=clicked45)
testbutton46 = pygame_gui.elements.UIButton(pygame.Rect(560, 65, 45 * 1.25, 40 * 1.25), "", manager, command=clicked46)
testbutton47 = pygame_gui.elements.UIButton(pygame.Rect(630, 65, 45 * 1.25, 40 * 1.25), "", manager, command=clicked47)
testbutton48 = pygame_gui.elements.UIButton(pygame.Rect(700, 65, 45 * 1.25, 40 * 1.25), "", manager, command=clicked48)
testbutton49 = pygame_gui.elements.UIButton(pygame.Rect(490, 10, 45 * 1.25, 40 * 1.25), "", manager, command=clicked49)
testbutton50 = pygame_gui.elements.UIButton(pygame.Rect(560, 10, 45 * 1.25, 40 * 1.25), "", manager, command=clicked50)
testbutton51 = pygame_gui.elements.UIButton(pygame.Rect(630, 10, 45 * 1.25, 40 * 1.25), "", manager, command=clicked51)
testbutton52 = pygame_gui.elements.UIButton(pygame.Rect(700, 10, 45 * 1.25, 40 * 1.25), "", manager, command=clicked52)

notetypeselected = "Normal"

notetype1 = "Normal"
notetype2 = "Normal"
notetype3 = "Normal"
notetype4 = "Normal"
notetype5 = "Normal"
notetype6 = "Normal"
notetype7 = "Normal"
notetype8 = "Normal"
notetype9 = "Normal"
notetype10 = "Normal"
notetype11 = "Normal"
notetype12 = "Normal"
notetype13 = "Normal"
notetype14 = "Normal"
notetype15 = "Normal"
notetype16 = "Normal"
notetype17 = "Normal"
notetype18 = "Normal"
notetype19 = "Normal"
notetype20 = "Normal"
notetype21 = "Normal"
notetype22 = "Normal"
notetype23 = "Normal"
notetype24 = "Normal"
notetype25 = "Normal"
notetype26 = "Normal"
notetype27 = "Normal"
notetype28 = "Normal"
notetype29 = "Normal"
notetype30 = "Normal"
notetype31 = "Normal"
notetype32 = "Normal"
notetype33 = "Normal"
notetype34 = "Normal"
notetype35 = "Normal"
notetype36 = "Normal"
notetype37 = "Normal"
notetype38 = "Normal"
notetype39 = "Normal"
notetype40 = "Normal"
notetype41 = "Normal"
notetype42 = "Normal"
notetype43 = "Normal"
notetype44 = "Normal"
notetype45 = "Normal"
notetype46 = "Normal"
notetype47 = "Normal"
notetype48 = "Normal"
notetype49 = "Normal"
notetype50 = "Normal"
notetype51 = "Normal"
notetype52 = "Normal"

showplayline = False
playline = PlayLine(490, 720)

def playit():
  global showplayline
  try:
    mixer.music.load("audio/songs/" + songinput.get_text() + ".mp3")
    mixer.music.set_volume(0.5)
    showplayline = True
    mixer.music.play()
  except:
    pygame_gui.windows.UIMessageWindow(rect=pygame.Rect(0,0, 100,100), html_message="Enter valid song name", manager=manager2, window_title="Error", always_on_top=True)

def stopit():
  global showplayline
  showplayline = False
  playline.resetpos()
  mixer.music.stop()

preveffect = False
fx = pygame.sprite.Group()

def previeweffect():
  global preveffect, lines, color, lights, fire, sm, pacles, rain, g1, g2, g3, vhs,fx
  if effectdrop.selected_option[0] == "Anime Lines":
    try:
      fx.remove(rain)
      rain.die()
    except:
      try:
        fx.remove(color)
        color.die()
      except:
        try:
          fx.remove(fire)
          fire.die()
        except:
          try:
            fx.remove(sm)
            sm.die()
          except:
            try:
              fx.remove(vhs)
              vhs.die()
            except:
              try:
                fx.remove(lights)
                lights.die()
              except:
                try:
                  fx.remove(pacles)
                  pacles.die()
                except:
                  try:
                    fx.remove(g1)
                    g1.die()
                  except:
                    try:
                      fx.remove(g2)
                      g2.die()
                    except:
                      try:
                        fx.remove(g3)
                        g3.die()
                      except:
                        pass
    lines = Lines(0,0)
    fx.add(lines)
  elif effectdrop.selected_option[0] == "Rain":
    try:
      fx.remove(lines)
      lines.die()
    except:
      try:
        fx.remove(color)
        color.die()
      except:
        try:
          fx.remove(fire)
          fire.die()
        except:
          try:
            fx.remove(sm)
            sm.die()
          except:
            try:
              fx.remove(vhs)
              vhs.die()
            except:
              try:
                fx.remove(lights)
                lights.die()
              except:
                try:
                  fx.remove(pacles)
                  pacles.die()
                except:
                  try:
                    fx.remove(g1)
                    g1.die()
                  except:
                    try:
                      fx.remove(g2)
                      g2.die()
                    except:
                      try:
                        fx.remove(g3)
                        g3.die()
                      except:
                        pass
    rain = Rain(0,0)
    fx.add(rain)
  elif effectdrop.selected_option[0] == "Color Wave":
    try:
      fx.remove(rain)
      rain.die()
    except:
      try:
        fx.remove(lines)
        lines.die()
      except:
        try:
          fx.remove(fire)
          fire.die()
        except:
          try:
            fx.remove(sm)
            sm.die()
          except:
            try:
              fx.remove(vhs)
              vhs.die()
            except:
              try:
                fx.remove(lights)
                lights.die()
              except:
                try:
                  fx.remove(pacles)
                  pacles.die()
                except:
                  try:
                    fx.remove(g1)
                    g1.die()
                  except:
                    try:
                      fx.remove(g2)
                      g2.die()
                    except:
                      try:
                        fx.remove(g3)
                        g3.die()
                      except:
                        pass
    color = ColorWave(0,0)
    fx.add(color)
  elif effectdrop.selected_option[0] == "Fire":
    try:
      fx.remove(rain)
      rain.die()
    except:
      try:
        fx.remove(color)
        color.die()
      except:
        try:
          fx.remove(lines)
          lines.die()
        except:
          try:
            fx.remove(sm)
            sm.die()
          except:
            try:
              fx.remove(vhs)
              vhs.die()
            except:
              try:
                fx.remove(lights)
                lights.die()
              except:
                try:
                  fx.remove(pacles)
                  pacles.die()
                except:
                  try:
                    fx.remove(g1)
                    g1.die()
                  except:
                    try:
                      fx.remove(g2)
                      g2.die()
                    except:
                      try:
                        fx.remove(g3)
                        g3.die()
                      except:
                        pass
    fire = Fire(0,0)
    fx.add(fire)
  elif effectdrop.selected_option[0] == "Smoke":
    try:
      rain.die()
    except:
      try:
        color.die()
      except:
        try:
          fire.die()
        except:
          try:
            lines.die()
          except:
            try:
              vhs.die()
            except:
              try:
                lights.die()
              except:
                try:
                  pacles.die()
                except:
                  try:
                    g1.die()
                  except:
                    try:
                      g2.die()
                    except:
                      try:
                        g3.die()
                      except:
                        pass
    sm = Smoke(0,0)
    fx.add(sm)
  elif effectdrop.selected_option[0] == "VHS":
    try:
      rain.die()
    except:
      try:
        color.die()
      except:
        try:
          fire.die()
        except:
          try:
            sm.die()
          except:
            try:
              lines.die()
            except:
              try:
                lights.die()
              except:
                try:
                  pacles.die()
                except:
                  try:
                    g1.die()
                  except:
                    try:
                      g2.die()
                    except:
                      try:
                        g3.die()
                      except:
                        pass
    vhs = Vhs(0,0)
    fx.add(vhs)
  elif effectdrop.selected_option[0] == "Lights":
    try:
      rain.die()
    except:
      try:
        color.die()
      except:
        try:
          fire.die()
        except:
          try:
            sm.die()
          except:
            try:
              vhs.die()
            except:
              try:
                lines.die()
              except:
                try:
                  pacles.die()
                except:
                  try:
                    g1.die()
                  except:
                    try:
                      g2.die()
                    except:
                      try:
                        g3.die()
                      except:
                        pass
    lights = Lights(0,0)
    fx.add(lights)
  elif effectdrop.selected_option[0] == "Particles":
    try:
      rain.die()
    except:
      try:
        color.die()
      except:
        try:
          fire.die()
        except:
          try:
            sm.die()
          except:
            try:
              vhs.die()
            except:
              try:
                lights.die()
              except:
                try:
                  lines.die()
                except:
                  try:
                    g1.die()
                  except:
                    try:
                      g2.die()
                    except:
                      try:
                        g3.die()
                      except:
                        pass
    pacles = Particles(0,0)
    fx.add(pacles)
  elif effectdrop.selected_option[0] == "Glitch 1":
    try:
      rain.die()
    except:
      try:
        color.die()
      except:
        try:
          fire.die()
        except:
          try:
            sm.die()
          except:
            try:
              vhs.die()
            except:
              try:
                lights.die()
              except:
                try:
                  pacles.die()
                except:
                  try:
                    lines.die()
                  except:
                    try:
                      g2.die()
                    except:
                      try:
                        g3.die()
                      except:
                        pass
    g1 = Glitch1(0,0)
    fx.add(g1)
  elif effectdrop.selected_option[0] == "Glitch 2":
    try:
      rain.die()
    except:
      try:
        color.die()
      except:
        try:
          fire.die()
        except:
          try:
            sm.die()
          except:
            try:
              vhs.die()
            except:
              try:
                lights.die()
              except:
                try:
                  pacles.die()
                except:
                  try:
                    g1.die()
                  except:
                    try:
                      lines.die()
                    except:
                      try:
                        g3.die()
                      except:
                        pass
    g2 = Glitch2(0,0)
    fx.add(g2)
  elif effectdrop.selected_option[0] == "Glitch 3":
    try:
      rain.die()
    except:
      try:
        color.die()
      except:
        try:
          fire.die()
        except:
          try:
            sm.die()
          except:
            try:
              vhs.die()
            except:
              try:
                lights.die()
              except:
                try:
                  pacles.die()
                except:
                  try:
                    g1.die()
                  except:
                    try:
                      g2.die()
                    except:
                      try:
                        lines.die()
                      except:
                        pass
    g3 = Glitch3(0,0)
    fx.add(g3)
  preveffect = True

def stopprevieweffect():
  global preveffect
  preveffect = False
  for fxs in fx:
    fx.remove(fxs)

playbutton = pygame_gui.elements.UIButton(pygame.Rect(1025, 670, 70, 50), "Play", manager=manager, command=playit)
stopbutton = pygame_gui.elements.UIButton(pygame.Rect(1100, 670, 70, 50), "Stop", manager=manager, command=stopit)
preveffectbtn = pygame_gui.elements.UIButton(pygame.Rect(0, 300, 100, 40), "Preview Effect", manager=manager, command=previeweffect)
stoppreveffectbtn = pygame_gui.elements.UIButton(pygame.Rect(100, 300, 100, 40), "Stop Preview", manager=manager, command=stopprevieweffect)

arrow1 = Arrow(760, 720, -100, 5)
arrow2 = Arrow(440, 720, -100, 5)

tickerint = 0

while True:
  k = pygame.mouse.get_pressed()
  somethingvalue = songspeedinput.get_current_value()
  refreshrate = clock.tick(60)/1000
  
  manager.update(refreshrate)
  manager2.update(refreshrate)

  screen.fill((0,0,0))
  arrow1.update()
  arrow2.update()

  #for key in keys:
    #key.draw()
  
  fps = round(clock.get_fps())

  fpstext = fontsmall.render("FPS: " + str(fps), False, (255,255,255), (0,0,0, 0.5))
  ramusagetxt = fontsmall.render("RAM USAGE: " + str(round((psutil.Process().memory_info().rss / 1024) / 1024)) + "MB (" + str(round((psutil.Process().memory_info().rss / psutil.virtual_memory().used) * 100, 2)) + "%)", False, (255,255,255), (0,0,0, 0.5))
  screen.blit(ramusagetxt, (110,0))
  screen.blit(fpstext, (110,20))

  screen.blit(songtext, (0, 110))
  screen.blit(songspeedtext, (0, 160))
  screen.blit(fontsmall.render(str(somethingvalue), False, (255,255,255)), (320, 160))
  screen.blit(notetext, (0, 210))
  screen.blit(effecttext, (0, 260))
  screen.blit(fontsmall.render(str(current_section+1),False, (255,255,255)), (1175, 650))
  
  manager.draw_ui(screen)

  note1 = Note(490, 670, notetype1)
  notetype_sections[current_section][0] = notetype1
  note2 = Note(560, 670, notetype2)
  notetype_sections[current_section][1] = notetype2
  note3 = Note(630, 670, notetype3)
  notetype_sections[current_section][2] = notetype3
  note4 = Note(700, 670, notetype4)
  notetype_sections[current_section][3] = notetype4
  note5 = Note(490, 615, notetype5)
  notetype_sections[current_section][4] = notetype5
  note6 = Note(560, 615, notetype6)
  notetype_sections[current_section][5] = notetype6
  note7 = Note(630, 615, notetype7)
  notetype_sections[current_section][6] = notetype7
  note8 = Note(700, 615, notetype8)
  notetype_sections[current_section][7] = notetype8
  note9 = Note(490, 560, notetype9)
  notetype_sections[current_section][8] = notetype9
  note10 = Note(560, 560, notetype10)
  notetype_sections[current_section][9] = notetype10
  note11 = Note(630, 560, notetype11)
  notetype_sections[current_section][10] = notetype11
  note12 = Note(700, 560, notetype12)
  notetype_sections[current_section][11] = notetype12
  note13 = Note(490, 505, notetype13)
  notetype_sections[current_section][12] = notetype13
  note14 = Note(560, 505, notetype14)
  notetype_sections[current_section][13] = notetype14
  note15 = Note(630, 505, notetype15)
  notetype_sections[current_section][14] = notetype15
  note16 = Note(700, 505, notetype16)
  notetype_sections[current_section][15] = notetype16
  note17 = Note(490, 450, notetype17)
  notetype_sections[current_section][16] = notetype17
  note18 = Note(560, 450, notetype18)
  notetype_sections[current_section][17] = notetype18
  note19 = Note(630, 450, notetype19)
  notetype_sections[current_section][18] = notetype19
  note20 = Note(700, 450, notetype20)
  notetype_sections[current_section][19] = notetype20
  note21 = Note(490, 395, notetype21)
  notetype_sections[current_section][20] = notetype21
  note22 = Note(560, 395, notetype22)
  notetype_sections[current_section][21] = notetype22
  note23 = Note(630, 395, notetype23)
  notetype_sections[current_section][22] = notetype23
  note24 = Note(700, 395, notetype24)
  notetype_sections[current_section][23] = notetype24
  note25 = Note(490, 340, notetype25)
  notetype_sections[current_section][24] = notetype25
  note26 = Note(560, 340, notetype26)
  notetype_sections[current_section][25] = notetype26
  note27 = Note(630, 340, notetype27)
  notetype_sections[current_section][26] = notetype27
  note28 = Note(700, 340, notetype28)
  notetype_sections[current_section][27] = notetype28
  note29 = Note(490, 285, notetype29)
  notetype_sections[current_section][28] = notetype29
  note30 = Note(560, 285, notetype30)
  notetype_sections[current_section][29] = notetype30
  note31 = Note(630, 285, notetype31)
  notetype_sections[current_section][30] = notetype31
  note32 = Note(700, 285, notetype32)
  notetype_sections[current_section][31] = notetype32
  note33 = Note(490, 230, notetype33)
  notetype_sections[current_section][32] = notetype33
  note34 = Note(560, 230, notetype34)
  notetype_sections[current_section][33] = notetype34
  note35 = Note(630, 230, notetype35)
  notetype_sections[current_section][34] = notetype35
  note36 = Note(700, 230, notetype36)
  notetype_sections[current_section][35] = notetype36
  note37 = Note(490, 175, notetype37)
  notetype_sections[current_section][36] = notetype37
  note38 = Note(560, 175, notetype38)
  notetype_sections[current_section][37] = notetype38
  note39 = Note(630, 175, notetype39)
  notetype_sections[current_section][38] = notetype39
  note40 = Note(700, 175, notetype40)
  notetype_sections[current_section][39] = notetype40
  note41 = Note(490, 120, notetype41)
  notetype_sections[current_section][40] = notetype41
  note42 = Note(560, 120, notetype42)
  notetype_sections[current_section][41] = notetype42
  note43 = Note(630, 120, notetype43)
  notetype_sections[current_section][42] = notetype43
  note44 = Note(700, 120, notetype44)
  notetype_sections[current_section][43] = notetype44
  note45 = Note(490, 65, notetype45)
  notetype_sections[current_section][44] = notetype45
  note46 = Note(560, 65, notetype46)
  notetype_sections[current_section][45] = notetype46
  note47 = Note(630, 65, notetype47)
  notetype_sections[current_section][46] = notetype47
  note48 = Note(700, 65, notetype48)
  notetype_sections[current_section][47] = notetype48
  note49 = Note(490, 10, notetype49)
  notetype_sections[current_section][48] = notetype49
  note50 = Note(560, 10, notetype50)
  notetype_sections[current_section][49] = notetype50
  note51 = Note(630, 10, notetype51)
  notetype_sections[current_section][50] = notetype51
  note52 = Note(700, 10, notetype52)
  notetype_sections[current_section][51] = notetype52

  if sections[current_section][0] == 1:
    if not cycledbefore1:
      notetype1 = notetypeselected
      cycledbefore1 = True
    note1.update()
  if sections[current_section][1] == 1:
    if not cycledbefore2:
      notetype2 = notetypeselected
      cycledbefore2 = True
    note2.update()
  if sections[current_section][2] == 1:
    if not cycledbefore3:
      notetype3 = notetypeselected
      cycledbefore3 = True
    note3.update()
  if sections[current_section][3] == 1:
    if not cycledbefore4:
      notetype4 = notetypeselected
      cycledbefore4 = True
    note4.update()
  if sections[current_section][4] == 1:
    if not cycledbefore5:
      notetype5 = notetypeselected
      cycledbefore5 = True
    note5.update()
  if sections[current_section][5] == 1:
    if not cycledbefore6:
      notetype6 = notetypeselected
      cycledbefore6 = True
    note6.update()
  if sections[current_section][6] == 1:
    if not cycledbefore7:
      notetype7 = notetypeselected
      cycledbefore7 = True
    note7.update()
  if sections[current_section][7] == 1:
    if not cycledbefore8:
      notetype8 = notetypeselected
      cycledbefore8 = True
    note8.update()
  if sections[current_section][8] == 1:
    if not cycledbefore9:
      notetype9 = notetypeselected
      cycledbefore9 = True
    note9.update()
  if sections[current_section][9] == 1:
    if not cycledbefore10:
      notetype10 = notetypeselected
      cycledbefore10 = True
    note10.update()
  if sections[current_section][10] == 1:
    if not cycledbefore11:
      notetype11 = notetypeselected
      cycledbefore11 = True
    note11.update()
  if sections[current_section][11] == 1:
    if not cycledbefore12:
      notetype12 = notetypeselected
      cycledbefore12 = True
    note12.update()
  if sections[current_section][12] == 1:
    if not cycledbefore13:
      notetype13 = notetypeselected
      cycledbefore13 = True
    note13.update()
  if sections[current_section][13] == 1:
    if not cycledbefore14:
      notetype14 = notetypeselected
      cycledbefore14 = True
    note14.update()
  if sections[current_section][14] == 1:
    if not cycledbefore15:
      notetype15 = notetypeselected
      cycledbefore15 = True
    note15.update()
  if sections[current_section][15] == 1:
    if not cycledbefore16:
      notetype16 = notetypeselected
      cycledbefore16 = True
    note16.update()
  if sections[current_section][16] == 1:
    if not cycledbefore17:
      notetype17 = notetypeselected
      cycledbefore17 = True
    note17.update()
  if sections[current_section][17] == 1:
    if not cycledbefore18:
      notetype18 = notetypeselected
      cycledbefore18 = True
    note18.update()
  if sections[current_section][18] == 1:
    if not cycledbefore19:
      notetype19 = notetypeselected
      cycledbefore19 = True
    note19.update()
  if sections[current_section][19] == 1:
    if not cycledbefore20:
      notetype20 = notetypeselected
      cycledbefore20 = True
    note20.update()
  if sections[current_section][20] == 1:
    if not cycledbefore21:
      notetype21 = notetypeselected
      cycledbefore21 = True
    note21.update()
  if sections[current_section][21] == 1:
    if not cycledbefore22:
      notetype22 = notetypeselected
      cycledbefore22 = True
    note22.update()
  if sections[current_section][22] == 1:
    if not cycledbefore23:
      notetype23 = notetypeselected
      cycledbefore23 = True
    note23.update()
  if sections[current_section][23] == 1:
    if not cycledbefore24:
      notetype24 = notetypeselected
      cycledbefore24 = True
    note24.update()
  if sections[current_section][24] == 1:
    if not cycledbefore25:
      notetype25 = notetypeselected
      cycledbefore25 = True
    note25.update()
  if sections[current_section][25] == 1:
    if not cycledbefore26:
      notetype26 = notetypeselected
      cycledbefore26 = True
    note26.update()
  if sections[current_section][26] == 1:
    if not cycledbefore27:
      notetype27 = notetypeselected
      cycledbefore27 = True
    note27.update()
  if sections[current_section][27] == 1:
    if not cycledbefore28:
      notetype28 = notetypeselected
      cycledbefore28 = True
    note28.update()
  if sections[current_section][28] == 1:
    if not cycledbefore29:
      notetype29 = notetypeselected
      cycledbefore29 = True
    note29.update()
  if sections[current_section][29] == 1:
    if not cycledbefore30:
      notetype30 = notetypeselected
      cycledbefore30 = True
    note30.update()
  if sections[current_section][30] == 1:
    if not cycledbefore31:
      notetype31 = notetypeselected
      cycledbefore31 = True
    note31.update()
  if sections[current_section][31] == 1:
    if not cycledbefore32:
      notetype32 = notetypeselected
      cycledbefore32 = True
    note32.update()
  if sections[current_section][32] == 1:
    if not cycledbefore33:
      notetype33 = notetypeselected
      cycledbefore33 = True
    note33.update()
  if sections[current_section][33] == 1:
    if not cycledbefore34:
      notetype34 = notetypeselected
      cycledbefore34 = True
    note34.update()
  if sections[current_section][34] == 1:
    if not cycledbefore35:
      notetype35 = notetypeselected
      cycledbefore35 = True
    note35.update()
  if sections[current_section][35] == 1:
    if not cycledbefore36:
      notetype36 = notetypeselected
      cycledbefore36 = True
    note36.update()
  if sections[current_section][36] == 1:
    if not cycledbefore37:
      notetype37 = notetypeselected
      cycledbefore37 = True
    note37.update()
  if sections[current_section][37] == 1:
    if not cycledbefore38:
      notetype38 = notetypeselected
      cycledbefore38 = True
    note38.update()
  if sections[current_section][38] == 1:
    if not cycledbefore39:
      notetype39 = notetypeselected
      cycledbefore39 = True
    note39.update()
  if sections[current_section][39] == 1:
    if not cycledbefore40:
      notetype40 = notetypeselected
      cycledbefore40 = True
    note40.update()
  if sections[current_section][40] == 1:
    if not cycledbefore41:
      notetype41 = notetypeselected
      cycledbefore41 = True
    note41.update()
  if sections[current_section][41] == 1:
    if not cycledbefore42:
      notetype42 = notetypeselected
      cycledbefore42 = True
    note42.update()
  if sections[current_section][42] == 1:
    if not cycledbefore43:
      notetype43 = notetypeselected
      cycledbefore43 = True
    note43.update()
  if sections[current_section][43] == 1:
    if not cycledbefore44:
      notetype44 = notetypeselected
      cycledbefore44 = True
    note44.update()
  if sections[current_section][44] == 1:
    if not cycledbefore45:
      notetype45 = notetypeselected
      cycledbefore45 = True
    note45.update()
  if sections[current_section][45] == 1:
    if not cycledbefore46:
      notetype46 = notetypeselected
      cycledbefore46 = True
    note46.update()
  if sections[current_section][46] == 1:
    if not cycledbefore47:
      notetype47 = notetypeselected
      cycledbefore47 = True
    note47.update()
  if sections[current_section][47] == 1:
    if not cycledbefore48:
      notetype48 = notetypeselected
      cycledbefore48 = True
    note48.update()
  if sections[current_section][48] == 1:
    if not cycledbefore49:
      notetype49 = notetypeselected
      cycledbefore49 = True
    note49.update()
  if sections[current_section][49] == 1:
    if not cycledbefore50:
      notetype50 = notetypeselected
      cycledbefore50 = True
    note50.update()
  if sections[current_section][50] == 1:
    if not cycledbefore51:
      notetype51 = notetypeselected
      cycledbefore51 = True
    note51.update()
  if sections[current_section][51] == 1:
    if not cycledbefore52:
      notetype52 = notetypeselected
      cycledbefore52 = True
    note52.update()

  if preveffect == True:
    if effectdrop.selected_option[0] == "Anime Lines":
      lines.update()
    elif effectdrop.selected_option[0] == "Rain":
      rain.update()
    elif effectdrop.selected_option[0] == "Color Wave":
      color.update()
    elif effectdrop.selected_option[0] == "Fire":
      fire.update()
    elif effectdrop.selected_option[0] == "Smoke":
      sm.update()
    elif effectdrop.selected_option[0] == "VHS":
      vhs.update()
    elif effectdrop.selected_option[0] == "Lights":
      lights.update()
    elif effectdrop.selected_option[0] == "Particles":
      pacles.update()
    elif effectdrop.selected_option[0] == "Glitch 1":
      g1.update()
    elif effectdrop.selected_option[0] == "Glitch 2":
      g2.update()
    elif effectdrop.selected_option[0] == "Glitch 3":
      g3.update()
    if not effectdrop.selected_option[0] == "None":
      fx.draw(screen)

  if showplayline == True:
    playline.update()

  manager2.draw_ui(screen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mixer.Sound("audio/sfx/confirm.mp3").play()
      confirmexit = UIConfirmationDialog(rect=pygame.Rect(screen.get_width()/2-200,screen.get_height()/2-75,400,100), action_long_desc="Did you save your chart?", manager=manager2, window_title="Exit Confirmation", action_short_name="Yes", object_id="#exitconf", always_on_top=True)
    if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
      if event.ui_element == confirmexit:
        pygame.quit()
        quit()
    if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
      if event.ui_element == notetypedrop:
        notetypeselected = notetypedrop.selected_option[1]
        #print(str(notetypeselected))
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      mixer.Sound("audio/sfx/buttonClick.mp3").play()
    if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
      mixer.Sound("audio/sfx/SliderMoved.mp3").play().set_volume(0.25)
    manager.process_events(event)
    manager2.process_events(event)

  tickerint += 1

  pygame.display.update()