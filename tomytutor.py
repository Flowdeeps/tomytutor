#!/usr/bin/env python

import array
import math

import pygame
import cairo
import ptext
import rsvg

from pygame.locals import *
from sys import exit

pygame.init()

# hide the cursor because we don't need that
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((640, 480), 0, 8) # the screen size will be 1280 * 800 in production
pygame.display.set_caption("Tomy Tutor OS v1.0")

# helper variables
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# set the default background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

# screen 1
ostext1 = "TOMY TUTOR"
ostext2 = "PLAY COMPUTER"
ostext3 = "OS v.1.0"

ostest1 = osfont.render(ostext1, True, red, (0, 0, 0, 0))
ostest2 = osfont.render(ostext2, True, red, (0, 0, 0, 0))
ostest3 = osfont.render(ostext3, True, red, (0, 0, 0, 0))

# screen 2

# screen 3

# screen 4

# screen 5

# screen 6

# screen 7

# screen 8

#set the fonts
pygame.font.init()
osfont = pygame.font.Font("fonts/frankfurter-solid.otf", 60)

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
		# we don't really need this one but I always forget what env I'm working in so have c as well as q to quit
		if event.key == K_c:
			exit()

	# update loop
	screen.blit(background, (0,0))
	screen.blit(ostest1, (80, 100))
	screen.blit(ostest2, (25, 180))
	screen.blit(ostest3, (170, 260))
	pygame.display.update()
