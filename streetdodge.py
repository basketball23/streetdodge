import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 100
FramePerSec = pygame.time.Clock()

ending = int(input('How many points do you want the game to end at?\n'))

music = int(input('Do you want music 1, 2, 3, 4, or 5?\n'))

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0


font = pygame.font.SysFont("Arial", 60)
font_small = pygame.font.SysFont("Arial", 20)
game_over = font.render("You crashed!!!", True, BLACK)

 
background = pygame.image.load("./media/AnimatedStreet.png")
 
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface.fill(WHITE)
pygame.display.set_caption("Street Dodge")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./media/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        press = pygame.key.get_pressed()
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        '''
        if press[K_SPACE]:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            time.sleep(0.15)
        '''
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./media/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-60)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.rect.move_ip(0,3)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)
                #Below here is the nitro boost code
        if pressed_keys[K_UP] and pressed_keys[K_LSHIFT]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN] and pressed_keys[K_LSHIFT]:
            self.rect.move_ip(0, 3)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] and pressed_keys[K_LSHIFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] and pressed_keys[K_LSHIFT]:
                  self.rect.move_ip(5, 0)

        if pressed_keys[K_w] and pressed_keys[K_LSHIFT]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_s] and pressed_keys[K_LSHIFT]:
            self.rect.move_ip(0, 3)
         
        if self.rect.left > 0:
              if pressed_keys[K_a] and pressed_keys[K_LSHIFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_d] and pressed_keys[K_LSHIFT]:
                  self.rect.move_ip(5, 0)
        
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = SCREEN_HEIGHT - 120
        if (self.rect.bottom < 0):
            self.rect.bottom = 120

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./media/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = P1.rect.center

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        self.rect.move_ip(0, -9)
        if self.rect.bottom > 0:
            if pressed_keys[K_SPACE]:
                self.rect.move_ip(0, -12)
        if self.rect.bottom < 0:
            self.rect.center = P1.rect.center

       
                           
P1 = Player()
E1 = Enemy()
shoot = Bullet()

enemies = pygame.sprite.Group()
enemies.add(E1)
bullets = pygame.sprite.Group()
bullets.add(shoot)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(shoot)
  
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
if music == 1:
    pygame.mixer.music.load('./media/gamemusic.mp3')
    pygame.mixer.music.play(-1)
elif music == 2:
    pygame.mixer.music.load('./media/TrapMusic.mp3')
    pygame.mixer.music.play(-1)
elif music == 3:
    pygame.mixer.music.load('./media/Gaming.mp3')
    pygame.mixer.music.play(-1)
elif music == 4:
    pygame.mixer.music.load('./media/Sportmusic.mp3')
    pygame.mixer.music.play(-1)
elif music == 5:
    pygame.mixer.music.load('./media/cyberpunkmusic.mp3')
    pygame.mixer.music.play(-1)


gameloop = True
while gameloop:
        
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.3     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    surface.blit(background, (0,0))
    scores = font_small.render("Your score is: " + str(SCORE), True, BLACK)
    hard = font_small.render("The game gets harder now....", True, BLACK)
    win = font.render('YOU WIN!!!', True, BLACK)
    finalscore = font_small.render('Your final score was: ' + str(SCORE), True, BLACK)
    surface.blit(scores, (10,10))
    
    if SCORE == 20:
        SPEED = SPEED + 0.05
        surface.blit(hard, (100, 300))
    if SCORE == 21:
        surface.blit(hard, (100, 300))
    if SCORE == 22:
        surface.blit(hard, (100, 300))
    if SCORE == 30:
        pygame.mixer.music.stop()
        pygame.mixer.Sound('./media/winning.wav').play()
        surface.fill(WHITE)
        surface.blit(win, (20, 250))
        surface.blit(finalscore, (100, 400))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill
        time.sleep(1.5)
        pygame.quit()
        sys.exit()

    if SCORE == ending:
        pygame.mixer.music.stop()
        pygame.mixer.Sound('./media/winning.wav').play()
        surface.fill(WHITE)
        surface.blit(win, (20, 250))
        surface.blit(finalscore, (100, 400))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill
        time.sleep(1.5)
        pygame.quit()
        sys.exit()

    
    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(shoot, enemies):
        SCORE = SCORE + 1
        E1.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        shoot.rect.center = P1.rect.center

    '''
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()
          pygame.mixer.Sound('./media/crash.wav').play()
          time.sleep(0.5)

          pressed = pygame.key.get_pressed()
        
          surface.fill(RED)
          surface.blit(game_over, (5,250))
          surface.blit(finalscore, (100, 400))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill()
    '''

    
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()
          pygame.mixer.Sound('./media/crash.wav').play()
          time.sleep(0.5)
                    
          surface.fill(RED)
          surface.blit(game_over, (5,250))
          surface.blit(finalscore, (100, 400))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(3)
          pygame.quit()
          sys.exit()
         
    pygame.display.update()
    FramePerSec.tick(FPS)