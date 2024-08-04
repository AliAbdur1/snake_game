import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)] # starting positions for the snake
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('snake_game_pics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('snake_game_pics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('snake_game_pics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('snake_game_pics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('snake_game_pics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('snake_game_pics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('snake_game_pics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('snake_game_pics/tail_left.png').convert_alpha()

        self.body_up = pygame.image.load('snake_game_pics/body_up.png').convert_alpha()
        self.body_right = pygame.image.load('snake_game_pics/body_right.png').convert_alpha()
        self.body_left = pygame.image.load('snake_game_pics/body_left.png').convert_alpha()
        self.body_down = pygame.image.load('snake_game_pics/body_down.png').convert_alpha()

        self.body_turn_up_right = pygame.image.load('snake_game_pics/body_turn_up_right.png').convert_alpha()
        self.body_turn_left = pygame.image.load('snake_game_pics/body_turn_left.png').convert_alpha()
        self.body_turn_down_right = pygame.image.load('snake_game_pics/body_turn_down_right.png').convert_alpha()
        self.body_turn_down_left = pygame.image.load('snake_game_pics/body_turn_down_left.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('snake_game_sounds/apple_crunch.mp3')

        

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body): # give index on what obj we are inside our list
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_up, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_right, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_turn_down_left,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_turn_left,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_turn_down_right,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_turn_up_right,block_rect)

            

            
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down






        # for block in self.body:
        #     x_pos = int(block.x * cell_size)
        #     y_pos = int(block.y * cell_size)
        #     block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        #     pygame.draw.rect(screen, (183, 191, 122), block_rect)
        #     # creates a body segment for the snake by cell_size

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] # stores body size of snake as a list
            body_copy.insert(0, body_copy[0] + self.direction) # creates a new body block by cell size
            self.body = body_copy[:] # adds it to the snake body list
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize() 

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        # pygame.draw.rect(screen, (200, 60, 40), fruit_rect)
        # create a rectangle

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y) # creates a 2D vector
        # places apple in a random position on screen
        
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit() # puts odject on screen
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: # checks if fruit and snake "head" are at same position
            self.fruit.randomize() # moves fruit to random position on screen
            self.snake.add_block() # if so, adds a new block to snake body
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize() # prevents fruit from appearing in snake body

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over() # checks if snake hits walls

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over() # checks if snake hits its own body


    def game_over(self):
        self.snake.reset()
        # pygame.quit()
        # sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3) # score is length of snake "- 3" because we start at 3 for out length
        score_surface = game_font.render(score_text, True,(56, 74, 12)) # Number, Anti-aliasing , color of text
        score_x = int(cell_size * cell_number - 60) # x position of score
        score_y = int(cell_size * cell_number - 40) # y position of score
        score_rect = score_surface.get_rect(center = (score_x, score_y)) # gets screen position for placing score 
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))# takes the midright of this rect and places on the left of our score rect
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width +6, apple_rect.height)


        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect) # renders score to screen
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen, (167, 209, 200), bg_rect, 2)
        

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('snake_game_pics/apple.png').convert_alpha() # assigns an image to our apple variable
game_font = pygame.font.Font('snake_game_fonts/The_Postgates.ttf', 25)

GREEN = (100, 200, 100)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #ends any code
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
    
    
    screen.fill(GREEN)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) # controlls game run speed