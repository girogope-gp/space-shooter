import pygame
from bullet import Bullet

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shoot_delay = 250  # Tiempo mínimo entre disparos en milisegundos
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Mantener al jugador dentro de la pantalla
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))

    def shoot(self, bullets):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            new_bullet = Bullet(self.rect.centerx - 2, self.rect.top)
            bullets.append(new_bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)