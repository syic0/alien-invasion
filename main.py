import sys
import pygame

from settings import Settings
from objects import Spacecraft

def run():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    spacecraft = Spacecraft(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        spacecraft.blitme()

        pygame.display.flip()

run()