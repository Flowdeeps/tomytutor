#!/usr/bin/env python

import array
import math

import pygame
import cairo
import ptext
#import numpy
import rsvg
#import gtk

from pygame.locals import *
from sys import exit

pygame.init()

# hide the cursor because we don't need that
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((640, 480), 0, 8)
pygame.display.set_caption("Tomy Tutor OS v1.0")

# set the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

pygame.font.init()

# loading screen
red = (255, 0, 0)
yellow = (255, 255, 0)
ostext1 = "TOMY TUTOR"
ostext2 = "PLAY COMPUTER"
ostext3 = "OS v.1.0"
osfont = pygame.font.Font("fonts/frankfurter-solid.otf", 60)
ostest1 = osfont.render(ostext1, True, red, (0, 0, 0, 0))
ostest2 = osfont.render(ostext2, True, red, (0, 0, 0, 0))
ostest3 = osfont.render(ostext3, True, red, (0, 0, 0, 0))

message = "FISH"
gamefont = pygame.font.Font("fonts/helvetica-black.otf", 80)
gametest = gamefont.render(message, True, (255, 255, 255), (0, 0, 0, 0))

# program loop
while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	# setup the keys
	# bind a quit key so it's possible to leave
	if event.type == KEYDOWN:
		if event.key == K_q:
			exit()
		if event.key == K_c:
			exit()

	# update loop
	screen.blit(background, (0,0))
	screen.blit(ostest1, (80, 100))
	screen.blit(ostest2, (25, 180))
	screen.blit(ostest3, (170, 260))
	pygame.display.update()
