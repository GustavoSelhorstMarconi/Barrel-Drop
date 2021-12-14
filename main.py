import pygame, random
from sys import exit
from enemies import Enemies
from player import Player

def collision():
  for sprite in enemies_group.sprites():
    if pygame.sprite.spritecollide(sprite, player_group.sprites(), False):
      return False
  return True

def display_score(text, text_size, pos_x, pos_y):
  font_score = pygame.font.SysFont('None', text_size)
  text_score = font.render(f'{text} {score}', True, (50, 50, 50))
  rect_score = text_score.get_rect(topleft = (pos_x, pos_y))
  screen.blit(text_score, rect_score)
  
screen_width = 900
screen_height = 600
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
screenActive = True
pointDifference = 0

# Background
background_sky = pygame.image.load('images/sky.png').convert_alpha()
background_sky = pygame.transform.scale(background_sky, (900, 450))

background_ground = pygame.image.load('images/ground.png').convert_alpha()
background_ground = pygame.transform.scale(background_ground, (900, 300))

# Groups
enemies_group = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()

# Player
player_group.add(Player())

# Timers
enemies_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemies_timer, 800)

# Texts
font = pygame.font.SysFont('None', 50)
text_render = font.render('You Lose', True, (250, 10, 10))
text_rect = text_render.get_rect(center = (screen_width / 2, screen_height / 2 - 50))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if screenActive:
      if event.type == enemies_timer:
        enemies_group.add(Enemies(random.choice([50, 150, 250, 350, 450, 550, 650, 750, 800]), -10, random.randint(5, 15), random.randint(100, 130)))
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        screenActive = True
        pointDifference = pygame.time.get_ticks() / 1000

  if screenActive:
    score = int(pygame.time.get_ticks() / 1000 - pointDifference)
    screen.blit(background_sky, (0, 0))
    screen.blit(background_ground, (0, 300))
    display_score('Score:' ,30, 10, 10)

    # Display enemies
    enemies_group.update()
    enemies_group.draw(screen)

    # Display player
    player_group.update()
    player_group.draw(screen)

    screenActive = collision()

  else:
    screen.fill((65, 105, 225))
    screen.blit(text_render, text_rect)
    display_score('Your score is:', 30, screen_width / 2 - 125, screen_height / 2 + 50)
    enemies_group.empty()

  pygame.display.update()
  clock.tick(60)