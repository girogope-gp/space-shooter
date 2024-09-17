import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(400, 500)
        self.enemies = []
        self.bullets = []
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def spawn_enemy(self):
        if len(self.enemies) < 5 and pygame.time.get_ticks() % 60 == 0:
            self.enemies.append(Enemy())

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        self.check_collisions()
        self.spawn_enemy()

        # Añadir esta línea para manejar el disparo
        self.handle_player_shoot()

    def handle_player_shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.shoot(self.bullets)

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def run(self):
        self.update()
        self.draw()