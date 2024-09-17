import pygame
import random

class Enemy:
    def __init__(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = 0

    def update(self):
        self.rect.y += 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)