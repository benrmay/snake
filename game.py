# Benjamin May
# Thanks to pygame library for making these things easier

import pygame
import random

from snake_obj import Snake

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BACKGROUND_COLOR = (0x00, 0x00, 0x00)
FRAMERATE = 32
ARROW_KEYS = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

game_clock = 0
# make sure the user is using WASD layout.... or else they will pay

def init_screen():
	pygame.init()
	pygame.display.set_caption("Ben May game")
	pygame.key.set_repeat(50,50) # continuing key press allows multiple presses
	return pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def play(snake, display):
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key in ARROW_KEYS):
					# make a move
					validMove = snake.move(event.key, display)
					if (validMove == False):
						print("game over!")
						pygame.quit()
					else:
						print("arrow button pressed")

			elif (event.type == pygame.QUIT):
				pygame.quit()
				return False




# to be completed later
def restart():
	# print out some text and whatnot
	while True:
		for event in pygame.event.get():
			if (event.key == pygame.K_SPACE):
				print("spacebar pressed")
				# play the game again
			elif (event.key == pygame.K_ESCAPE):
				print("ESC pressed")
				# quit the game

def main():
	display = init_screen()
	display.fill(BACKGROUND_COLOR)
	snake = Snake()
	game_clock = pygame.time.Clock()
	
	keep_playing = play(snake, display)
	if (keep_playing == True):
		play(snake, display)
	else:
		return 1

# run the game!
main()
