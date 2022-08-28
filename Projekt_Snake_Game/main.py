import pygame
import knoepfe
import spiel

pygame.init()
#Spielfenster erstllen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

#Font für die Schrift
font = pygame.font.SysFont("arialblack", 25)
TEXT_COL = (0, 0, 0)

#Laden der Bilder 
start_img_img = pygame.image.load("img/start.png").convert_alpha()
anleitung_img = pygame.image.load("img/anleitung.png").convert_alpha()

esc_img = pygame.image.load("img/esc.png").convert_alpha()
w_img = pygame.image.load("img/w.png").convert_alpha()
up_img = pygame.image.load("img/up.png").convert_alpha()
d_img = pygame.image.load("img/d.png").convert_alpha()
right_img = pygame.image.load("img/right.png").convert_alpha()
s_img = pygame.image.load("img/s.png").convert_alpha()
down_img = pygame.image.load("img/down.png").convert_alpha()
a_img = pygame.image.load("img/a.png").convert_alpha()
left_img = pygame.image.load("img/left.png").convert_alpha()

exit_img = pygame.image.load("img/exit.png").convert_alpha()
back_img = pygame.image.load('img/back.png').convert_alpha()

#Knöpfe Instanzen erstellen
start_img_button = knoepfe.Button(400, 100, start_img_img, 1)
handbook_button = knoepfe.Button(400, 225, anleitung_img, 1)
quit_button = knoepfe.Button(400, 350, exit_img, 1)
back_button = knoepfe.Button(400, 450, back_img, 1)

def text_schreiben(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#Spiel schleife
menue_state = 'main'
run = True
while run:
  screen.fill((34, 177, 76))
  #Menü
  if menue_state == "main":
    if start_img_button.zeichne(screen):
      game = spiel.Spiel(screen)
      game.start()
    if handbook_button.zeichne(screen):
      menue_state = "handbook"
    if quit_button.zeichne(screen):
      run = False
  #Optionen unter Menü
  if menue_state == "handbook":

    text_schreiben("Snake Anleitung",font,TEXT_COL,150,80)
    text_schreiben("Die Snake muss den Apfel essen damit Sie größer wird",font,TEXT_COL,150,125)
    text_schreiben("Der Score der am Ende eine Runde angezeigt wird",font,TEXT_COL,150,150)

    screen.blit(esc_img,(250,200))
    text_schreiben(": zurück zum Menü",font,TEXT_COL,300,200)

    screen.blit(w_img,(200,250))
    screen.blit(up_img,(250,250))
    text_schreiben(": die Snake bewegt sich nach oben",font,TEXT_COL,300,250)

    screen.blit(d_img,(200,300))
    screen.blit(right_img,(250,300))
    text_schreiben(": die Snake bewegt sich nach rechts",font,TEXT_COL,300,300)

    screen.blit(s_img,(200,350))
    screen.blit(down_img,(250,350))
    text_schreiben(": die Snake bewegt sich nach unten",font,TEXT_COL,300,350)

    screen.blit(a_img,(200,400))
    screen.blit(left_img,(250,400))
    text_schreiben(": die Snake bewegt sich nach links",font,TEXT_COL,300,400)

    if back_button.zeichne(screen):
      menue_state = "main"
  
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.type == pygame.QUIT:
        run = False

  pygame.display.update()
pygame.quit()