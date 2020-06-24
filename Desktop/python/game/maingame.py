import pygame, sys, os
from pygame.locals import *
import time
import random
import emoji

#part1
pygame.init()
white = (255,255,255)
black= (100,0,0)
red = (255,0,0)
green= (0,255,0)
window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Snake Game:Created by Sharad!!')

font = pygame.font.SysFont(None, 25, bold=True)

def myquit():
	pygame.quit()
	sys.exit(0)


#part2
clock = pygame.time.Clock()
FPS = 5  #Use for refreshment of screen
blockSize= 20
noPixel = 0

#part 3

def snake(blockSize,snakeList):

	for size in snakeList:
		pygame.draw.rect(gameDisplay, black,[size[0]+5,size[1],blockSize,blockSize])
		#doubt above

def message_to_screen(msg,color):
	font = pygame.font.SysFont('Times New Roman',35,False,False)
	screen_text = font.render(msg,True,color)
	gameDisplay.blit(screen_text,[190,250])
	 
	
	#doubt above


#part 4
def gameLoop():
	gameExit = False
	gameOver = False

	lead_x=window_width/2
	lead_y=window_height/2

	change_pixels_of_x = 0
	change_pixels_of_y = 0

	snakeList = []
	snakeLength = 1
	score = 0
	clock = pygame.time.Clock()

	randomAppleX = round(random.randrange(0 , window_width-blockSize))
	randomAppleY = round(random.randrange(0 , window_height-blockSize))

	while not gameExit:
		while gameOver == True:
			gameDisplay.fill(white)
			message_to_screen("Game over!!!press c to play again",red)
			#print(emoji.emojize(":zipper-mouth_face:"))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					gameExit = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()

			

#logic 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					myquit()
				leftArrow = event.key == pygame.K_LEFT
				rightArrow = event.key == pygame.K_RIGHT
				upArrow = event.key == pygame.K_UP
				downArrow = event.key == pygame.K_DOWN

				if leftArrow:
					change_pixels_of_x = -blockSize
					change_pixels_of_y = noPixel
				elif rightArrow:
					change_pixels_of_x = blockSize
					change_pixels_of_y = noPixel
				elif upArrow:
					change_pixels_of_y = -blockSize
					change_pixels_of_x = noPixel
				elif downArrow:
					change_pixels_of_y = blockSize
					change_pixels_of_x = noPixel

#logic 2
			if lead_x >=window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
					#doubt above
				gameOver = True

		lead_x +=change_pixels_of_x
		lead_y +=change_pixels_of_y
		score +=1

		gameDisplay.fill(white)

		AppleThickness = 20

#logic 3
		print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
		pygame.draw.rect(gameDisplay,red,[randomAppleX,randomAppleY,blockSize,blockSize])

			#doubt above

		allspriteslist = []
		allspriteslist.append(lead_x)
		allspriteslist.append(lead_y)
		snakeList.append(allspriteslist)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		for eachSegment in snakeList [:-1]:
			if eachSegment == allspriteslist:
				gameOver = True


		font = pygame.font.SysFont('Calibri',40,False,False)
		text = font.render("Score : "+ str(score),True,green)
		gameDisplay.blit(text,[600,100])


#logic 4
		snake(blockSize, snakeList)

		pygame.display.update()

#logic 5
			
		if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
			if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
				randomAppleX = round(random.randrange(0 , window_width-blockSize))
				randomAppleY = round(random.randrange(0 , window_height-blockSize))
					# doubt above
				snakeLength +=1

		

		clock.tick(FPS)

	pygame.quit()
	quit()

gameLoop()










