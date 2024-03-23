import random, pygame, math
from settings import *


class Entity:
    def __init__(self, pos):
        self.screen_size = screen_size
        self.pos = pos
        self.vel = pygame.math.Vector2(random.randint(-1, 1), random.randint(-1, 1))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = 40
        self.max_dist = self.size

        self.gravity = gravity

    def check_atom_collisions(self, target_pos, dt, mouse=1):
        diff = pygame.math.Vector2(target_pos - self.pos)
        dist = math.sqrt(diff[0]**2 + diff[1]**2)

        if dist < self.max_dist:
            try:
                force = (self.size - dist)
                self.pos -= pygame.math.Vector2.normalize((target_pos - self.pos)) * force
            except:
                pass
        self.check_wall_collisions()

    def apply_gravity(self, dt):
        self.vel.y += self.gravity * dt
        self.vel *= air_friction

    def check_wall_collisions(self):
        if self.pos.x <= self.size/2:
            self.pos.x = self.size/2
            self.vel.x = 0
        if self.pos.y <= self.size/2:
            self.pos.y = self.size/2
            self.vel.y = 0
        if self.pos.x >= self.screen_size[0] - self.size/2:
            self.pos.x = self.screen_size[0] - self.size/2
            self.vel.x = 0
        if self.pos.y >= self.screen_size[1] - self.size/2:
            self.pos.y = self.screen_size[1] - self.size/2
            self.vel.y = 0

    def update(self, dt):
        self.apply_gravity(dt)
        self.pos += self.vel * dt
