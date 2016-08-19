import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PURPLE = (200,30,240)

colors = []

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

for i in range(100):
	r = random.randint(50,255)
	g = random.randint(50,255)
	b = random.randint(50,255)
	colors.append((r,g,b))

color = colors[0]

class Ball():
	def __init__(self, xpos, ypos):
		#self.radius = random.randint(20,30)
		self.radius = 10
		self.xpos = xpos
		self.ypos = ypos
		self.xspeed = random.randint(-10,10)
		self.yspeed = random.randint(-10,10)
		self.color = PURPLE
		self.n = 0
	
	def flashBounce(self, screen, colors, screenWidth, screenHeight):
		
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight
		self.colors = colors
		self.screen = screen
		self.n = random.randint(0,99)
		#self.color = colors[self.n]
		# drawing circle
		#pygame.draw.circle(self.screen, color, (self.xpos,self.ypos), self.radius, 0)
		
	
		if(self.ypos >= self.screenHeight-self.radius):
			self.xspeed = self.xspeed
			self.yspeed = -1* self.yspeed
			self.color = self.colors[self.n]
		
		elif(self.ypos <=self.radius):
			self.xspeed = self.xspeed
			self.yspeed = -1 * self.yspeed
			self.color = self.colors[self.n]
		
		elif(self.xpos <= self.radius):
			self.xspeed = -1 * self.xspeed
			self.yspeed = self.yspeed
			self.color = self.colors[self.n]
		
		elif(self.xpos >= self.screenWidth-self.radius):
			self.xspeed = -1 * self.xspeed
			self.yspeed = self.yspeed
			self.color = self.colors[self.n]
		
		else:
			self.xspeed = self.xspeed
			self.yspeed = self.yspeed
		
		
		self.xpos = self.xpos + self.xspeed
		self.ypos = self.ypos + self.yspeed
		pygame.draw.circle(self.screen, self.color, (self.xpos,self.ypos), self.radius, 0)
		



# WRITE YOUR CODE HERE


x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT //2
x2 = SCREEN_WIDTH // 2
y2 = SCREEN_HEIGHT //2


ballsNumber = 3000

balls = []

for i in range(ballsNumber):
	balls.append(Ball(x,y))


while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(BLACK)
	#def __init__(self, radius, xpos, ypos, xspeed, yspeed):
	
	#def flashBounce(self, screen, colors, screenWidth, screenHeight):
	
	
	for j in range(ballsNumber):
		balls[j].flashBounce(screen, colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(120)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE