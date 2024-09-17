import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.is_active = True
        self.font = pygame.font.Font(None, 48)

    def draw(self):
        self.screen.fill((0, 0, 0))
        title = self.font.render("Space Shooter", True, (255, 255, 255))
        start = self.font.render("Presione SPACE para iniciar", True, (255, 255, 255))
        self.screen.blit(title, (300, 200))
        self.screen.blit(start, (250, 300))

    def run(self):
        self.draw()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_active = False