import pygame
from player import Player
from constants import *


def main():
    # initialise pygame and window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # track FPS
    clock = pygame.time.Clock()
    dt = 0  # time change (sec)

    # object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # initialise objects
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # update updatables
        for obj in updatable:
            obj.update(dt)
            
        # render
        screen.fill("black")
        
        # draw drawables
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000  # update time


if __name__ == "__main__":
    main()
