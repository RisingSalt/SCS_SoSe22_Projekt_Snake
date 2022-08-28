import pygame
import time
from pygame.locals import * 
import random

SIZE = 50

class Food:
    def __init__(self, parent_screen):
        self.food = pygame.image.load("img/food_block.png").convert_alpha()
        self.parent_screen = parent_screen
        self.food_x = random.randint(0,18)*SIZE
        self.food_y = random.randint(0,15)*SIZE

    def food_erstellen(self):
        self.parent_screen.blit(self.food,(self.food_x,self.food_y))
        pygame.display.update()

    def move(self):
        self.food_x = random.randint(0,18)*SIZE
        self.food_y = random.randint(0,15)*SIZE

class Snake:
    def __init__(self, parent_screen, groesse):
        self.groesse = groesse
        self.parent_screen = parent_screen
        self.snake = pygame.image.load("img/snake_block.png").convert_alpha()
        self.snake_x = [SIZE]*groesse
        self.snake_y = [SIZE]*groesse
        self.richtung = 'right'

    def erhoehe_groesse(self):
        self.groesse += 1
        self.snake_x.append(-1)
        self.snake_y.append(-1)

    def up(self):
        self.richtung = 'up'
    def down(self):
        self.richtung = 'down'
    def right(self):
        self.richtung = 'right'
    def left(self):
        self.richtung = 'left'

    def snake_erstellen(self):
        self.parent_screen.fill((34, 177, 76))#Clear
        for i in range(self.groesse):
            self.parent_screen.blit(self.snake,(self.snake_x[i],self.snake_y[i]))
        pygame.display.update()

    def move(self):

        for i in range(self.groesse-1,0,-1):
            self.snake_x[i] = self.snake_x[i - 1]
            self.snake_y[i] = self.snake_y[i - 1]

        if self.richtung == 'up':
            self.snake_y[0] -= SIZE
        if self.richtung == 'down':
            self.snake_y[0] += SIZE
        if self.richtung == 'right':
            self.snake_x[0] += SIZE
        if self.richtung == 'left':
            self.snake_x[0] -= SIZE
        
        self.snake_erstellen()

class Spiel:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.snake = Snake(self.parent_screen, 1)
        self.snake.snake_erstellen()
        self.food = Food(self.parent_screen)
        self.food.food_erstellen()

    def kollision(self, x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def ausfuehren(self):
        self.snake.move()
        self.food.food_erstellen()
        #self.score_anzeige()
        pygame.display.update()

        if self.kollision(self.snake.snake_x[0], self.snake.snake_y[0], self.food.food_x, self.food.food_y):
            self.snake.erhoehe_groesse()
            self.food.move()

        for i in range(1,self.snake.groesse):
            if self.kollision(self.snake.snake_x[0], self.snake.snake_y[0], self.snake.snake_x[i], self.snake.snake_y[i]):
                raise 'Game Over'

        if not (0 <= self.snake.snake_x[0] <= 950 and 0 <= self.snake.snake_y[0] <= 750):
            raise 'Game Over'

    #Der Score war am Flackern und wurde, um vor Epilepsie Anfallen zu vermeiden auskommentiert
    #Der Score wir noch am ende einer Runde angezeigt 
    def score_anzeige(self):
        font = pygame.font.SysFont("arialblack", 25)
        TEXT_COL = (0, 0, 0)
        score = font.render(f"Score: {self.snake.groesse}", True, TEXT_COL)
        self.parent_screen.blit(score,(10,10))

    def game_over_anzeige(self):
        self.parent_screen.fill((34, 177, 76))
        font = pygame.font.SysFont("arialblack", 25)
        TEXT_COL = (0, 0, 0)
        endscore = font.render(f"Score: {self.snake.groesse}", True, TEXT_COL)
        self.parent_screen.blit(endscore,(300,225))
        text_a = font.render("Neustarten (Enter)", True, TEXT_COL)
        text_b = font.render("Zurück zum Menü (ESC)", True, TEXT_COL)
        self.parent_screen.blit(text_a,(300,250))
        self.parent_screen.blit(text_b,(300,275))
        pygame.display.flip()

    def spiel_neustart(self):
        self.snake = Snake(self.parent_screen, 1)
        self.food = Food(self.parent_screen)

    def start(self):
        run = True
        pause = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pause = False
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w and not self.snake.richtung == 'down':
                        self.snake.up()
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s and not self.snake.richtung == 'up': 
                        self.snake.down()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d and not self.snake.richtung == 'left':
                        self.snake.right()
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a and not self.snake.richtung == 'right':
                        self.snake.left()
            try:
                if not pause:
                    self.ausfuehren()
            except Exception as e:
                self.game_over_anzeige()
                pause = True
                self.spiel_neustart()

            time.sleep(.2)