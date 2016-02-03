import pygame
import sys
import random
import jet
from colors import *
pygame.init()

screen_size = height, width = 600 , 480

screen = pygame.display.set_mode(screen_size)
player = jet.jet()
player.init(height,width)
clock = pygame.time.Clock()
astroids = []
while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT : sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.x_change = - 10
			if event.key == pygame.K_RIGHT:
				player.x_change =  10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.x_change = - 0
			if event.key == pygame.K_RIGHT:
				player.x_change =  0
	screen.fill(GREEN)
	player.move(screen)
	pygame.display.flip()
	clock.tick(50)
