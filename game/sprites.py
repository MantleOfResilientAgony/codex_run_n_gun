import pygame
import random

# Game sprite classes

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(midbottom=pos)
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -15
        self.on_ground = False

    def update(self, keys_pressed):
        # Horizontal movement
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Apply gravity
        self.vel_y += 1  # gravity constant
        self.rect.y += self.vel_y

        # Keep player on screen
        if self.rect.bottom >= 540:
            self.rect.bottom = 540
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def shoot(self, bullets_group):
        bullet = Bullet(self.rect.midright)
        bullets_group.add(bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > 800:
            self.kill()
