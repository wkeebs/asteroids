import pygame
from typing import override
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)
    
    @override
    def update(self, dt):
        self.position += dt * self.velocity