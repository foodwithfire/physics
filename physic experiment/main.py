import pygame, sys, atom, random
from settings import *

screen = pygame.display.set_mode(screen_size)

atoms = []
AtomClass = atom.Atom

clock = pygame.time.Clock()

while True:
    dt = clock.tick(60)
    screen.fill("white")
    if pygame.mouse.get_pressed()[0]:
        atoms.append(AtomClass(pygame.math.Vector2(pygame.mouse.get_pos())))

    for atom in atoms:
        atom.update(dt)
        for other_atom in atoms:
            if atom != other_atom:
                atom.check_atom_collisions(other_atom.pos, dt, 2)

        pygame.draw.circle(screen, atom.color, (atom.pos[0], atom.pos[1]), atom.size/2)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
