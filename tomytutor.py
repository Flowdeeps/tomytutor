#!/usr/bin/env python

import pygame

from pygame.locals import *
from sys import exit

pygame.init()

# bind a quit key so it's possible to leave

# hide the cursor because we don't need that
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((640, 480), 0, 8)
pygame.display.set_caption("Tomy Tutor OS v1.0")

# set the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

# program loop
while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	# setup the keys
	if event.type == KEYDOWN:
		if event.key == K_q:
			exit()

	# update loop
	screen.blit(background, (0,0))
	pygame.display.update()
