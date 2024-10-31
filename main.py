from constants import *
import pygame


def main():
    # initialise pygame and window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # track FPS
    clock = pygame.time.Clock()
    dt = 0 # time change (sec)

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # black screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # update time


if __name__ == "__main__":
    main()
