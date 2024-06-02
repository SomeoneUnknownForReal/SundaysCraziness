import pygame, pygame_gui, time, psutil, random, os
from pygame import mixer
from functools import cache

here = os.path.dirname(os.path.abspath(__file__))

@cache
def get_version():
  with open("changelog.txt", "r") as f:
    return f.readline()

version = get_version()

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption(f"Sunday's Craziness | Currently Playing: Bike - Tanger | Version: {version}")
manager = pygame_gui.UIManager((1280,720), None, True, None, "en", None)

background = pygame.image.load("img/bike/background.png")
pygame.transform.scale(background, (1280, 720))

noteSizeMul = 1.25
songSpeed = 3
songsfiledir = "audio/songs/"
chartsdir = "charts/"
pressything = 0

score = 0
misses = 0
combo = 0
bestcombo = 0
totalhit = 0
percantage = 0
songName = "thermodynamix"
songNotes = 0
songStrums = 0
botplay = False # Ustaw to na False, żeby gra nie grała za siebie

beat = 0
debugmode = True
paused = 0

pygame.font.init()
font = pygame.font.Font("fonts/default.ttf", 48)
fontmedium = pygame.font.Font("fonts/default.ttf", 36)
fontsmall = pygame.font.Font("fonts/debug.ttf", 16)

save_score = 0
save_percantage = 0
save_misses = 0
save_totalhit = 0
save_bestcombo = 0

defaultkey1x = 490
defaultkey1y = 600
defaultkey2x = 560
defaultkey2y = 600
defaultkey3x = 630
defaultkey3y = 600
defaultkey4x = 700
defaultkey4y = 600

key1x = defaultkey1x
key1y = defaultkey1y
key2x = defaultkey2x
key2y = defaultkey2y
key3x = defaultkey3x
key3y = defaultkey3y
key4x = defaultkey4x
key4y = defaultkey4y

key1col = (255,255,255)
key2col = (255,255,255)
key3col = (255,255,255)
key4col = (255,255,255)

key1presscol = (220,220,220)
key2presscol = (220,220,220)
key3presscol = (220,220,220)
key4presscol = (220,220,220)

mixer.init()

clock = pygame.time.Clock()

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

class Key():
  def __init__(self, x, y, color1, color2, key):
    self.x = x
    self.y = y
    self.color1 = color1
    self.color2 = color2
    self.key = key
    self.rect = pygame.Rect(self.x, self.y, 45 * noteSizeMul + pressything, 40 * noteSizeMul + pressything)
    self.handled = False

fx = pygame.sprite.Group()

keys = [
  Key(key1x, key1y,key1col,key1presscol, pygame.K_a),
  Key(key2x, key2y,key2col,key2presscol, pygame.K_s),
  Key(key3x, key3y,key3col,key3presscol, pygame.K_k),
  Key(key4x, key4y,key4col,key4presscol, pygame.K_l)
]

def load(map):
  global songNotes, songStrums, fx, songSpeed
  global songName, save_score, save_bestcombo, save_percantage, save_misses, save_totalhit

  with open("saves/" + songName + ".txt", "a+") as f:
    save_score = sum([int(x) for x in f.readline().split()])
    save_percantage = sum([float(x) for x in f.readline().split()])
    save_misses = sum([int(x) for x in f.readline().split()])
    save_totalhit = sum([int(x) for x in f.readline().split()])
    save_bestcombo = sum([int(x) for x in f.readline().split()])
  
  with open("fxsettings/" + songName + ".txt") as f:
    oneline = f.readline()
    if oneline.lower() == "lines" or oneline.lower() == "line" or oneline.lower() == "anime lines" or oneline.lower() == "anime line":
      lines = Lines(0,0)
      fx.add(lines)
    elif oneline.lower() == "rain":
      rain = Rain(0,0)
      fx.add(rain)
    elif oneline.lower() == "colorwave" or oneline.lower() == "color wave":
      colorwave = ColorWave(0,0)
      fx.add(colorwave)
    elif oneline.lower() == "fire":
      fire = Fire(0,0)
      fx.add(fire)
    elif oneline.lower() == "glitch1" or oneline.lower() == "glitch 1":
      glitch1 = Glitch1(0,0)
      fx.add(glitch1)
    elif oneline.lower() == "glitch2" or oneline.lower() == "glitch 2":
      glitch2 = Glitch2(0,0)
      fx.add(glitch2)
    elif oneline.lower() == "glitch3" or oneline.lower() == "glitch 3":
      glitch3 = Glitch3(0,0)
      fx.add(glitch3)
    elif oneline.lower() == "lights":
      lights = Lights(0,0)
      fx.add(lights)
    elif oneline.lower() == "particles":
      particles = Particles(0,0)
      fx.add(particles)
    elif oneline.lower() == "smoke":
      smoke = Smoke(0,0)
      fx.add(smoke)
    elif oneline.lower() == "vhs":
      vhs = Vhs(0,0)
      fx.add(vhs)

  rects = []
  music = mixer.music
  music.set_volume(0.5)
  music.load(songsfiledir + map + ".mp3")
  mixer.music.play()
  f = open(chartsdir + map + ".txt", "r")
  songSpeed = int(f.readline())
  data = f.readlines()

  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == '0':
        rects.append(pygame.Rect(keys[x].rect.x,y * -100,40 * noteSizeMul,40 * noteSizeMul))
        songNotes += 1
      if data[y][x] == "|":
        rects.append(pygame.Rect(keys[x].rect.x,y * -100,20 * noteSizeMul,40 * noteSizeMul * songSpeed))
        songStrums += 1
      if data[y][x] == "x" or data[y][x] == "X":
        rects.append(pygame.Rect(keys[x].rect.x,y * -100,45 * noteSizeMul,45 * noteSizeMul))
  return rects

def pause():
  global paused
  paused = 1

def unpause():
  global paused
  paused = 0

lowfps = 99999999
highfps = 0

def countdown():
  screen.blit(background, background.get_rect())
  s = pygame.Surface((1280,720))
  s.set_alpha(128)
  s.fill((0,0,0))
  screen.blit(s, (0,0))
  s2 = pygame.Surface((340,720))
  s2.set_alpha(148)
  s2.fill((0,0,0))
  screen.blit(s2, (screen.get_width()/2-180,0))
  screen.blit(font.render("3", False, (255,255,255)), (screen.get_width()/2-15,screen.get_height()/2-15))
  pygame.display.flip()
  time.sleep(1)
  screen.blit(background, background.get_rect())
  s = pygame.Surface((1280,720))
  s.set_alpha(128)
  s.fill((0,0,0))
  screen.blit(s, (0,0))
  s2 = pygame.Surface((340,720))
  s2.set_alpha(148)
  s2.fill((0,0,0))
  screen.blit(s2, (screen.get_width()/2-180,0))
  screen.blit(font.render("2", False, (255,255,255)), (screen.get_width()/2-15,screen.get_height()/2-15))
  pygame.display.flip()
  time.sleep(1)
  screen.blit(background, background.get_rect())
  s = pygame.Surface((1280,720))
  s.set_alpha(128)
  s.fill((0,0,0))
  screen.blit(s, (0,0))
  s2 = pygame.Surface((340,720))
  s2.set_alpha(148)
  s2.fill((0,0,0))
  screen.blit(s2, (screen.get_width()/2-180,0))
  screen.blit(font.render("1", False, (255,255,255)), (screen.get_width()/2-15,screen.get_height()/2-15))
  pygame.display.flip()
  time.sleep(1)
  screen.blit(background, background.get_rect())
  s = pygame.Surface((1280,720))
  s.set_alpha(128)
  s.fill((0,0,0))
  screen.blit(s, (0,0))
  s2 = pygame.Surface((340,720))
  s2.set_alpha(148)
  s2.fill((0,0,0))
  screen.blit(s2, (screen.get_width()/2-180,0))
  screen.blit(font.render("GO!", False, (255,255,255)), (screen.get_width()/2-15,screen.get_height()/2-15))
  pygame.display.flip()
  time.sleep(1)
countdown()

health = 100.0
healthbar = pygame_gui.elements.UIProgressBar(pygame.Rect(0, 0, 400, 20), manager=manager)

def gameover():
  gameovermanager = pygame_gui.UIManager((1280,720), None, True, None, "en", None)
  mixer.music.stop()
  while True:
    screen.fill((0,0,0))
    pygame_gui.elements.UIButton(pygame.Rect(screen.get_width()/2-50, screen.get_height()/2-20, 100, 40), "Restart", manager=gameovermanager, command=game)

def game():
  global misses, score, health, totalhit, bestcombo, save_bestcombo, save_percantage, percantage, save_misses, save_totalhit, beat, map_rect, keys, pressything, combo, fps, lowfps, highfps
  map_rect = load(songName)
  maxscore = (50 * songNotes) + (10 * songStrums)
  running = True
  while running:
    healthbar.set_current_progress(health)
    if health <= 0.0:
      quit()
    #clock.tick(120)
    refreshrate = clock.get_fps()/1000
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        with open("saves/" + songName + ".txt", "w+") as f:
          if save_score < score:
            f.write(str(score) + "\n")
          else:
            f.write("0\n")
          if save_percantage < percantage:
            f.write(str(percantage) + "\n")
          else:
            f.write("0.00\n")
          if save_misses > misses:
            f.write(str(misses) + "\n")
          else:
            f.write("99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n")
          if save_totalhit < totalhit:
            f.write(str(totalhit) + "\n")
          else:
            f.write("0\n")
          if save_bestcombo < bestcombo:
            f.write(str(bestcombo))
          else:
            f.write("0")
        pygame.quit()
        quit()
  
    manager.update(refreshrate)

    screen.blit(background, background.get_rect())
    s = pygame.Surface((1280,720))
    s.set_alpha(128)
    s.fill((0,0,0))
    screen.blit(s, (0,0))
    s2 = pygame.Surface((340,720))
    s2.set_alpha(148)
    s2.fill((0,0,0))
    screen.blit(s2, (screen.get_width()/2-180,0))
  
    k = pygame.key.get_pressed()
    for key in keys:
      if k[key.key]:
        pressything = 10
        pygame.draw.rect(screen,key.color2,key.rect)
        key.handled = False
      if not k[key.key]:
        pressything = 0
        pygame.draw.rect(screen,key.color1,key.rect)
        key.handled = True

    if beat % 10 == 0:
      hitinfo = fontmedium.render("", False, (255,255,255))
    for rect in map_rect:
      if rect.width > (40 * noteSizeMul):
        pygame.draw.rect(screen,(100,0,0), rect)
      else:
        pygame.draw.rect(screen,(255,255,255), rect)
      rect.y += songSpeed * 4
      if botplay == False:
        for key in keys:
          if key.rect.colliderect(rect) and not key.handled:
            if rect.width > (40 * noteSizeMul):
              hitinfo = fontmedium.render("Bad Note!", False, (255,255,255))
              map_rect.remove(rect)
              randomstr = str(random.randint(1, 3))
              sound = mixer.Sound("audio/sfx/missnote/missnote"+ randomstr + ".mp3")
              sound.set_volume(1)
              sound.play()
              score -= 10
              misses += 1
              health -= 10.0
              key.handled = True
              break
            elif rect.width == (20 * noteSizeMul):
              hitinfo = fontmedium.render("Strum!", False, (255,255,255))
              score += 10
              map_rect.remove(rect)
              totalhit += 1
              combo += 1
              if combo > bestcombo:
                bestcombo = combo
              key.handled = True
              break
            else:
              randomstr = str(random.randint(1, 4))
              sound = mixer.Sound("audio/sfx/keyClick/keyClick"+ randomstr + ".mp3")
              sound.set_volume(1)
              sound.play()
              if key.rect.y == rect.y or key.rect.y - 5 == rect.y or key.rect.y + 5 == rect.y or key.rect.y + 1 == rect.y or key.rect.y + 2 == rect.y or key.rect.y + 3 == rect.y or key.rect.y + 4 == rect.y or key.rect.y - 4 == rect.y or key.rect.y - 3 == rect.y or key.rect.y - 2 == rect.y or key.rect.y - 1 == rect.y:
                hitinfo = fontmedium.render("Perfect!!!", False, (255,255,255))
                score += 50
              elif key.rect.y - 10 == rect.y or key.rect.y - 9 == rect.y or key.rect.y - 8 == rect.y or key.rect.y - 7 == rect.y or key.rect.y - 6 == rect.y or key.rect.y + 10 == rect.y or key.rect.y + 9 == rect.y or key.rect.y + 8 == rect.y or key.rect.y + 7 == rect.y or key.rect.y + 6 == rect.y:
                hitinfo = fontmedium.render("Good!", False, (255,255,255))
                score += 30
              elif key.rect.y - 15 == rect.y or key.rect.y - 14 == rect.y or key.rect.y - 13 == rect.y or key.rect.y - 12 == rect.y or key.rect.y - 1 == rect.y or key.rect.y + 15 == rect.y or key.rect.y + 14 == rect.y or key.rect.y + 13 == rect.y or key.rect.y + 12 == rect.y or key.rect.y + 11 == rect.y:
                hitinfo = fontmedium.render("Decent", False, (255,255,255))
                score += 20
              else:
                hitinfo = fontmedium.render("Bad!", False, (255,255,255))
                score += 10
              map_rect.remove(rect)
              totalhit += 1
              combo += 1
              if combo > bestcombo:
                bestcombo = combo
              key.handled = True
              break
          if rect.y > (key.rect.y + 50):
            if rect.width > (40 * noteSizeMul):
              break
            hitinfo = fontmedium.render("Miss!", False, (255,255,255))
            randomstr = str(random.randint(1, 3))
            sound = mixer.Sound("audio/sfx/missnote/missnote"+ randomstr + ".mp3")
            sound.set_volume(1)
            sound.play()
            misses += 1
            score -= 10
            health -= 1.0
            combo = 0
            map_rect.remove(rect)
            break
      else:
        hitinfo = fontmedium.render("CPU SHOWCASE", False, (255,255,255))
        for key in keys:
          if key.rect.colliderect(rect) and not rect.width > (40 * noteSizeMul):
            if rect.width == (40 * noteSizeMul):
              randomstr = str(random.randint(1, 4))
              sound = mixer.Sound("audio/sfx/keyClick/keyClick"+ randomstr + ".mp3")
              sound.set_volume(1)
              sound.play()
            map_rect.remove(rect)
  
    screen.blit(hitinfo, (screen.get_width()/2-(hitinfo.get_width()/2), screen.get_height()/2-(hitinfo.get_height()/2)))

    fx.draw(screen)
    fx.update()

    if misses == 0 and totalhit == 0:
      percenttext = fontmedium.render("Acc: 100% (100%)", False, (255,255,255))
    elif totalhit == 0 and misses > 0:
      percenttext = fontmedium.render("Acc: 0% (0%)", False, (255,255,255))
    else:
      if percantage < 0:
        percenttext = fontmedium.render("Acc: 0% (0%)", False, (255,255,255))
      else:
        percantage = round(100 - ((misses / totalhit) * 100), 2)
        totalpercent = round(100 - ((misses / songNotes) * 100), 2)
        percenttext = fontmedium.render("Acc: " + str(percantage) + "% (" + str(totalpercent) + "%)", False, (255,255,255))
        if percantage > save_percantage:
          screen.blit(fontmedium.render("Best Accuracy!", False, (255,255,255)), (800, 320))

    scoretext = font.render("Score: " + str(score) + "/" + str(maxscore), False, (255,255,255))
    missestext = fontmedium.render("Misses: " + str(misses), False, (255,255,255))
    combotext = fontmedium.render("Combo: " + str(combo), False, (255,255,255))
    bestcombotext = fontmedium.render("Best Combo: " + str(bestcombo), False, (255,255,255))
    totalhittext = fontmedium.render("Total Hit: " + str(totalhit) + "/" + str(songNotes), False, (255,255,255))
    versiontext = fontsmall.render("v" + version + " | Made by Someone", False, (255, 255, 255), (0,0,0, 0.5))
    fps = round(clock.get_fps())
    if beat <= 10:
      fps = 60
    if not beat <= 10:
      if fps < lowfps:
        lowfps = fps
      if fps > highfps:
        highfps = fps

    debugtext = fontsmall.render("Debug mode enabled", False, (255,255,255), (0,0,0, 0.5))
    beattext = fontsmall.render("Beat: " + str(beat), False, (255,255,255), (0,0,0, 0.5))
    fpstext = fontsmall.render("FPS: " + str(fps) + " | LOWEST: " + str(lowfps) + ", HIGHEST: " + str(highfps), False, (255,255,255), (0,0,0, 0.5))
    ramusagetxt = fontsmall.render("RAM USAGE: " + str(round((psutil.Process().memory_info().rss / 1024) / 1024)) + "MB (" + str(round((psutil.Process().memory_info().rss / psutil.virtual_memory().used) * 100, 2)) + "%)", False, (255,255,255), (0,0,0, 0.5))
    cputesttext = fontsmall.render("CPU SHOWCASE MODE: " + str(botplay), False, (255,255,255), (0,0,0))

    screen.blit(percenttext, (25, 320))
    screen.blit(scoretext, (25,360))
    screen.blit(missestext, (25, 420))
    screen.blit(combotext, (25, 460))
    screen.blit(bestcombotext, (25, 520))
    screen.blit(totalhittext, (25, 580))
    screen.blit(versiontext, (25, 700))
    if debugmode == True:
      screen.blit(debugtext, (25, 25))
      screen.blit(beattext, (25, 45))
      screen.blit(fpstext, (25, 65))
      screen.blit(ramusagetxt, (25, 85))
      screen.blit(cputesttext, (25,105))
  
    if score > save_score:
      screen.blit(fontmedium.render("Best Score!", False, (255,255,255)), (800, 360))
  
    if misses < save_misses:
      screen.blit(fontmedium.render("Lowest Misses!", False, (255,255,255)), (800, 420))
  
    if bestcombo > save_bestcombo:
      screen.blit(fontmedium.render("New Best Combo!", False, (255,255,255)), (800, 520))
  
    if totalhit > save_totalhit:
      screen.blit(fontmedium.render("Biggest Total Hit!", False, (255,255,255)), (800, 580))

    manager.draw_ui(screen) 

    beat += 1
    if beat <= 200:
      screen.blit(font.render("A    S    K    L", False, (0,0,0)), (500,600))
    pygame.display.flip()
game()