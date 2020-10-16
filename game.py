
import pygame
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Get Big')

################################################################################
# VARIABLES
################################################################################

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

CHARACTER_WIDTH = 40
CHARACTER_HEIGHT = 40

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40
enemy_dead = False

player_square_size=50
AI_square_size=50

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player Variables
player_x = 50
player_y = 50

# Target Variables
target_x = 250
target_y = 400

# TODO: Add variables for the "enemy" character
points = 0

# Other variables
velocity = 10
enemy_velocity = 10
points = 0
enemy_points = 0

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

circles = []

class Circle:
    def __init__(self):
        self.y = random.randint(30,350)
        self.x = random.randint(30,450)
        self.pos = (self.x, self.y)
        self.color = GREEN
        self.size = 10
    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.size)
 
################################################################################
# HELPER FUNCTIONS
################################################################################

def is_colliding(x1, y1, x2, y2, width, height, width2, height2):
    """Returns True if two shapes are colliding, or False otherwise"""
    # If one rectangle is on left side of the other 
    if (x1 >= x2 + width2) or (x2 >= x1 + width):
        return False
  
    # If one rectangle is above the other
    if (y1 >= y2 + height2) or (y2 >= y1 + height):
        return False
  
    return True

def draw_text(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

      #if event.key == K_a:

################################################################################
# GAME LOOP
################################################################################

for i in range(30):
    sizes = [10,15,20]
    current_circle=Circle()
    current_circle.size=random.choice(sizes)
    circles.append(current_circle)

# Run until the user asks to quit

random_circle = random.choice(circles)
random_y=random_circle.y
random_x=random_circle.x

running = True
while running:
    # Advance the clock
    pygame.time.delay(20)

    # Did the user click the window close button?
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #random.choose(circle)
    #dx, dy = (circlex - ax, circley - ay)

    keys = pygame.key.get_pressed()

    # Update the player
    if keys[pygame.K_LEFT]:
        player_x -= velocity
    if keys[pygame.K_RIGHT]:
        player_x += velocity
    if keys[pygame.K_UP]:
        player_y -= velocity
    if keys[pygame.K_DOWN]:
        player_y += velocity

    # Update the target



    #if is_colliding(target_x, target_y, random_x, random_y, ENEMY_WIDTH, ENEMY_HEIGHT, ):
    #    target_x=250
     #   target_y=250

    # TODO: Update the enemy's y position based on its velocity

    # If target went off the screen, reset it
    if target_y > SCREEN_HEIGHT: 
        target_y = 0
        target_x = (SCREEN_WIDTH - CHARACTER_WIDTH)

    # TODO: If enemy went off the screen, reset it

    # If player collides with target, reset it & increment points
    if is_colliding(player_x, player_y, target_x, target_y, CHARACTER_WIDTH, CHARACTER_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT):
        #target_y = 0
        #target_x = (SCREEN_WIDTH - CHARACTER_WIDTH)
        CHARACTER_WIDTH+=enemy_points
        CHARACTER_HEIGHT+=enemy_points
        if(points > enemy_points):
            enemy_dead=True
    
    # TODO: If player collides with enemy, reset it & set points to 0
    
    # Fill screen with white
    screen.fill(WHITE)
    
    for circle in circles:
        circle.draw()
    
    for circle in circles:
        if is_colliding(player_x, player_y, circle.x, circle.y, CHARACTER_WIDTH, CHARACTER_HEIGHT, circle.size, circle.size):
            circles.remove(circle)
            if circle.size == 10:
                CHARACTER_WIDTH+=2
                CHARACTER_HEIGHT+=2
                points += 2
            elif circle.size == 15:
                CHARACTER_WIDTH+=5
                CHARACTER_HEIGHT+=5
                points += 5
            elif circle.size == 20:
                CHARACTER_WIDTH += 10
                CHARACTER_HEIGHT += 10
                points += 10

    for circle in circles:
        if is_colliding(target_x, target_y, circle.x, circle.y, ENEMY_WIDTH, ENEMY_HEIGHT, circle.size, circle.size):
            circles.remove(circle)
            if circle.size == 10:
                ENEMY_WIDTH+=2
                ENEMY_HEIGHT+=2
                enemy_points += 2
            elif circle.size == 15:
                ENEMY_WIDTH+=5
                ENEMY_HEIGHT+=5
                enemy_points += 5
            elif circle.size == 20:
                ENEMY_WIDTH += 10
                ENEMY_HEIGHT += 10
                enemy_points += 10

    # Draw the player as a blue square
    pygame.draw.rect(screen, BLUE, (player_x, player_y, CHARACTER_WIDTH, CHARACTER_HEIGHT))
    #enemy_rect=pygame.draw
    if enemy_dead==False:
        pygame.draw.rect(screen, RED, (target_x, target_y, ENEMY_WIDTH, ENEMY_HEIGHT))
    elif enemy_dead==True:
        pass

    # Draw the points
    draw_text(text=f'Score: {points}', color=BLACK, font_size=24, x=20, y=20)

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()