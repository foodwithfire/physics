import pygame, sys, entity, random
from settings import *

screen = pygame.display.set_mode(screen_size)

entities = []
EntityClass = entity.Entity

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)
    screen.fill("white")
    if pygame.mouse.get_pressed()[0]:
        entities.append(EntityClass(pygame.math.Vector2(pygame.mouse.get_pos())))

    for entity in entities:
        entity.update(dt)
        for other_entity in entities:
            if entity != other_entity:
                entity.check_atom_collisions(other_entity.pos, dt, 2)

        pygame.draw.circle(screen, entity.color, (entity.pos[0], entity.pos[1]), entity.size/2)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
