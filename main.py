import pygame
from player import Player
from constants import *


def main():
    # initialise pygame and window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # track FPS
    clock = pygame.time.Clock()
    dt = 0  # time change (sec)

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update player
        player.update(dt)
        
        # render
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000  # update time


if __name__ == "__main__":
    main()
