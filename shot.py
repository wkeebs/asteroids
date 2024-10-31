import pygame
from typing import override
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    @override
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    @override
    def update(self, dt):
        self.position += dt * self.velocity