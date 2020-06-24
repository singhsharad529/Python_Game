import pygame, sys, os
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()

#initializing the diplay window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong")

# starting coordinates of the paddle




def exitoragain():
	font = pygame.font.SysFont('Calibri',30,False,False)
	text = font.render("Press q for exit and c to restart",True,green)
	screen.blit(text,[250,250])
	 

	


def drawrect(screen,x,y):
	if x <= 0:
		x = 0
	if x >= 690:
		x = 699
	pygame.draw.rect(screen,red,[x,y,100,20])


#game's main loop
def main():
	rect_x = 400
	rect_y = 580

#initial speed of the padding

	rect_change_x =0
	rect_change_y = 0

#initial postition of the ball

	ball_x = 50
	ball_y = 50

#speed of the ball
	ball_change_x = 5
	ball_change_y = 5

	score = 0

	done = False
	gameOver=False
	clock = pygame.time.Clock()
	while not done:
		while gameOver == True:
			screen.fill(white)
			exitoragain()
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					done = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						done = True
						gameOver = False
					if event.key == pygame.K_c:
						main()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					rect_change_x = -6
				elif event.key == pygame.K_RIGHT:
					rect_change_x = 6



		screen.fill(white)
		rect_x += rect_change_x
		rect_y += rect_change_y

		ball_x += ball_change_x
		ball_y += ball_change_y


		if ball_x <0:
			ball_x = 0
			ball_change_x = ball_change_x * -1
		elif ball_x > 785:
			ball_x = 785
			ball_change_x = ball_change_x * -1
		elif ball_y <0:
			ball_y = 0
			ball_change_y = ball_change_y* -1
		elif ball_x > rect_x and ball_x<rect_x+100 and ball_y == 565:
			ball_change_y  = ball_change_y* -1
			score = score +1
		elif ball_y>600:
			ball_change_y = ball_change_y* -1
			score = 0
			gameOver=True
			exitoragain()
		
		
		pygame.draw.rect(screen,blue,[ball_x,ball_y,15,15])


		drawrect(screen,rect_x,rect_y)

	#score board
		font = pygame.font.SysFont('Calibri',35,False,False)
		text = font.render("Score : "+ str(score),True,red)

		screen.blit(text,[600,100])
		pygame.display.flip()
		clock.tick(60)

	pygame.quit()


main()











