import pygame
import random
from typing import override
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    @override
    def update(self, dt):
        self.position += dt * self.velocity
    
    def split(self):
        self.kill() # gg
        
        # small asteroid
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        # calculate new directions
        rand_angle = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(rand_angle)
        velocity_two = self.velocity.rotate(-rand_angle)
        
        # calculate new radii
        radius_one = self.radius - ASTEROID_MIN_RADIUS
        radius_two = self.radius - ASTEROID_MIN_RADIUS
        
        # create new asteroids
        asteroid_one = Asteroid(self.position.x, self.position.y, radius_one)
        asteroid_two = Asteroid(self.position.x, self.position.y, radius_two)
        
        # speed up and angle new asteroids
        asteroid_one.velocity = velocity_one * 1.2
        asteroid_two.velocity = velocity_two * 1.2