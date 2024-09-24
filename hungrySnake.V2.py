import pygame
import random
from pygame.locals import *


SCREEN_SIZE = 1000

screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
clock = pygame.time.Clock()

# Initialization of the game
screen.fill((100, 100, 100))
pygame.display.flip()

  
# set the image which to be displayed on screen 
snake_head_img = pygame.image.load('images/snake_head.png') 
snake_body_img = pygame.image.load('images/snake_body.png') 
snake_tail_img = pygame.image.load('images/snake_tail.png')

apple_img = pygame.image.load('images/apple.png')
#snake_tail_img = pygame.transform.rotate(snake_tail_img, 180)
  

# Set the size for the image
SIZE = 50  #50 is the default, but it is a bit choppy/big
DEFAULT_IMAGE_SIZE = (SIZE, SIZE)
START_LOCATION = (300, 300)
step = SIZE/2



def scale_to_game(image):
    return pygame.transform.scale(image, (SIZE, SIZE))



# Scale the image to your needed size
if SIZE != 50:
    snake_head_img = scale_to_game(snake_head_img)
    snake_body_img = scale_to_game(snake_body_img)
    snake_tail_img = scale_to_game(snake_tail_img)
    apple_img      = scale_to_game(apple_img)
    
    
    
    
    
    
    
    
    
    
    
    
class Coordinate():
    x = -1
    y = -1
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y


def next_step(direction, speed, coordinate):
    x = coordinate.x
    y = coordinate.y
    if direction == 'down':
        y = y + speed
    elif direction == 'up':
        y = y - speed
    elif direction == 'left':
        x = x - speed
    elif direction == 'right':
        x = x + speed
    else:
        print('something went wrong!  I do not understand the direction ' + direction)
    new_coordinate = Coordinate(x, y)
    return new_coordinate

class Vector():
    def __init__(self, the_direction, the_coordinate):
        self.direction = the_direction
        self.coordinate = the_coordinate
    
        
SNAKE_STEP = SIZE/2


#Our snake Sprite representation
class HungrySnake():
    #A list of vectors representing the head, body-parts and tail
    # where the first element is always the head and the last element
    # is the tail
    path = []
    
    #The snake will have a head + size body parts and a tail
    #The snake will start at `start_position` and the rest of the
    # snake will follow and always be pointing `down`
    def __init__(self, size, start_position):
        current_coordinate = start_position
        #Add the Head
        self.path = []
        self.path.append(start_position)
        #Add the Body coordinate
        for i in range(0, size):
            current_coordinate = next_step('down', SNAKE_STEP, current_coordinate)
            self.path.append(current_coordinate)
            
    
        #Add the tail
        current_coordinate = next_step('down', SNAKE_STEP, current_coordinate)
        self.path.append(current_coordinate)
    
new_snake = HungrySnake(1, Coordinate(1,1))
    


class Move:
    x = -1
    y = -1
    direction = "down"
    def __init__(self, x_pos, y_pos, dir):
        self.x = x_pos
        self.y = y_pos
        self.direction = dir
        
class Food():
    x = -1
    y = -1
    image = -1
    visible = True
    
    def draw(self, screen):
        if self.visible:
          screen.blit(self.image, (self.x, self.y))
        else:
          pygame.draw.rect(screen, (255, 255, 255), 
                 pygame.Rect(self.x, self.y, SIZE, SIZE))

    def hide(self, screen):
        (blank_image, (self.x, self.y))
    
    def isEaten(self, a_snake):
      return False
    
SNAKE_SIZE=30

class Snake():
    #snake_path = [(300, 300),(300, 250), (300, 200)]
    path2 = []    
    for i in range(0, SNAKE_SIZE):
        path2.append(Move(START_LOCATION[0], START_LOCATION[1]-(i*step), "down"))
        
    direction = "down"
    
    def draw(self, screen):
        self.draw_tail(screen)
        self.draw_head(screen)
        self.draw_body(screen)
        
    def draw_head(self, screen):
        self.draw_segment(screen, self.path2[0], snake_head_img)
        
    def draw_body(self, screen):
        for path_elt in self.path2[1:-1]:
            self.draw_segment(screen, path_elt,  snake_body_img)
    
    def draw_tail(self, screen):
        the_move = self.path2[-1]
        self.draw_segment(screen, the_move, snake_tail_img)
    
    def draw_segment(self, screen, move, image):
        copy_image = image
        #"down" is default - no change
        rotation = 0
        if move.direction == "up":
            rotation = 180
        elif move.direction == "left":
            rotation = 270
        elif move.direction == "right":
            rotation = 90
        else:
            rotation = 0
        copy_image = pygame.transform.rotate(copy_image, rotation)
        screen.blit(copy_image, (move.x, move.y))
        
    def finds_food(self, f_list):
         snake_x1 = self.path2[0].x
         snake_x2 = self.path2[0].x + step
         snake_y1 = self.path2[0].y
         snake_y2 = self.path2[0].y + step
         print('find food? ' + str(snake_x1) + ' ' + str(snake_y1))
         for a_food in f_list:
             if (a_food.x >= snake_x1 and
                 a_food.x <= snake_x2 and
                 a_food.y >= snake_y1 and
                 a_food.y <= snake_y2):
                 print('Found food!')
                 return a_food
            
    
    def eat_food(self, a_food, food_list):
         #chomp sound?
         a_food.visible = False
         food_list.remove(a_food)
         self.grow()
    
    def grow(self):
        m = self.path2[-1]
        self.path2.append(Move(m.x, m.y+step, "down"))
             
          
        
    def move(self):
        new_move = 1
        new_x = self.path2[0].x
        new_y = self.path2[0].y
        new_move = Move(self.path2[0].x, self.path2[0].y, self.direction)        
        if self.direction == "down":
            new_move.y = self.path2[0].y + step
        if self.direction == "up":
            new_move.y = self.path2[0].y - step
        elif self.direction == "left":
            new_move.x = self.path2[0].x - step
        elif self.direction == "right":
            new_move.x = self.path2[0].x + step
        self.path2.insert(0, new_move)
        self.path2 = self.path2[:-1]  #remove last element
            

def make_random_food(num_food):
  new_food_list = []
  for i in range(0, num_food):
      random_food = Food()
      random_food.x = random.randrange(0, SCREEN_SIZE-SIZE)
      random_food.y = random.randrange(0, SCREEN_SIZE-SIZE)
      random_food.image = apple_img
      new_food_list.append(random_food)
  return new_food_list
      
food_list = make_random_food(4)

global_counter = 0

player_snake = Snake()

# Snake Game animation loop
while True:
    for event in pygame.event.get():
        # Close window event
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        elif event.type == KEYDOWN and event.key == K_DOWN: 
                #  the bird flaps up
                print("Change to down")
                player_snake.direction = "down"
        elif event.type == KEYUP and event.key == K_UP:
                #  the bird flaps up
                print("Change to up")
                player_snake.direction = "up"
        elif event.type == KEYUP and event.key == K_LEFT:
                #  the bird flaps up
                print("Change to left")
                player_snake.direction = "left"
        elif event.type == KEYUP and event.key == K_RIGHT:
                #  the bird flaps up
                print("Change to right")
                player_snake.direction = "right"
                
                
        
            
    pygame.display.update()
    global_counter = global_counter + 1
    
    # Calculate the delta time between two frames (in seconds)
    delta = clock.tick(60) / 1000
    if global_counter % step == 0:
        #print("move here")
        player_snake.move()

        found_food = player_snake.finds_food(food_list)
        if found_food != None:
            player_snake.eat_food(found_food, food_list)
            if not food_list: #all food is eaten
                print("YOU WIN!!!")
                food_list = make_random_food(6)


    # Draw the bird and score on the screen
    screen.fill((255, 255, 255))
    player_snake.draw(screen)
    #bird.print_info()
    
    for a_food in food_list:
      a_food.draw(screen)
    
    pygame.display.flip()