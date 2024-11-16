import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        split_velocity1 = self.velocity.rotate(angle)
        split_velocity2 = self.velocity.rotate(-angle)

        smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        smaller_asteroid1 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
        smaller_asteroid2 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)

        smaller_asteroid1.velocity = split_velocity1 * 1.2
        smaller_asteroid2.velocity = split_velocity2 * 1.2
