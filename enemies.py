import pygame

class Enemies(pygame.sprite.Sprite):
  def __init__(self, pos_x, pos_y, speed, size):
    super().__init__()
    self.image = pygame.image.load('images/enemies/barrel.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (size, size * 1.103))
    self.rect = self.image.get_rect(center = (pos_x, pos_y))
    self.speed = speed

  def movement(self):
    self.speed += 0.15
    self.rect.y += self.speed

    if self.rect.y >= 650:
      self.kill()

  def update(self):
    self.movement()