import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image_normal = pygame.image.load('images/player/player_normal.png').convert_alpha()
    self.image_walk = pygame.image.load('images/player/player_walk.png').convert_alpha()
    self.image = self.image_normal
    self.rect = self.image.get_rect(center = (450, 450))
    self.direction = 0
    self.speed = 8
    self.right_turn = 0

    self.index_image = 0
    self.image_list = [self.image_normal, self.image_walk]

  def input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
      self.direction = self.speed
      self.right_turn = 1
    elif keys[pygame.K_LEFT]:
      self.direction = self.speed * -1
      self.right_turn = -1
    else:
      self.direction = 0
      self.right_turn = 0

  def animation(self):
    self.index_image += 0.1
    if self.index_image > len(self.image_list):
      self.index_image = 0
    if self.right_turn != 0:
      self.image = self.image_list[int(self.index_image)]
    else:
      self.image = self.image_list[0]
    if self.right_turn == -1:
      self.image = pygame.transform.flip(self.image, True, False)
  
  def movement(self):
    self.rect.x += self.direction

    if self.rect.right >= 900:
      self.rect.right = 900
    elif self.rect.left <= 0:
      self.rect.left = 0
  
  def update(self):
    self.input()
    self.animation()
    self.movement()