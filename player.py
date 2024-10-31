import pygame
from typing import override
from constants import *
from circleshape import CircleShape
from shot import Shot

def smooth(x):
    """ Smoothing function for momentum calculation """
    return (x * 3) ** 2 / 3

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__shot_timer = 0
        self.__momentum_timer = 0
        self.__momentum_direction = pygame.Vector2(0, 0)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    @override
    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.__shot_timer -= dt
        self.__momentum_timer = max(self.__momentum_timer - dt, 0)

        # momentum movement
        self.position += self.__momentum_direction * smooth(self.__momentum_timer)
            
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        direction = 1 if dt > 0 else -1 # forward/backwards momentum
        self.__momentum_direction = pygame.Vector2(0, direction).rotate(self.rotation)
        self.__momentum_timer = 1

    def shoot(self):
        if self.__shot_timer > 0:
            # rate limiting
            return

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(
            self.rotation) * PLAYER_SHOOT_SPEED
        self.__shot_timer = PLAYER_SHOOT_COOLDOWN
