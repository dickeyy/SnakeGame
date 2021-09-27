# Import stuff
import pygame
import time
import random

# initaite the game 
pygame.init()
print("GAME INITIATED...")

# define the colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (102, 102, 102)
 
# make the screen size
dis_width = 600
dis_height = 400

# Set the display window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by kyle')

# Set up the clock
clock = pygame.time.Clock()

# Set the snake stats
snake_block = 10
snake_speed = 13

# Set up the fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

print("STYLES AND VARS COMPLIED...")

# Define the score variable
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Draw the snake and display 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])
 
# Define message styling
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

print("COMPONETS GENERATED...")

# Define the Loop
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    # Generate food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    printWord = 1
    printWord2 = 1
    
    # Detect game over and what happens if it is over
    while not game_over:
        if printWord == 1:
            print("GAME STARTED...")
            printWord += 1
            pass
        else:
            pass
        while game_close == True:
            if printWord2 == 1:
                print("Snake Died... Awaiting Response...")
                printWord2 += 1
                pass
            else:
                pass
            dis.fill(black)
            message("You Lost! Press R to Play Again or Q to Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("Game Quit by Client")
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        print("Game restarting...")
                        gameLoop()

        # Define what happens on key strokes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        # Define when the games over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Update the screen and score 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        # Register snake speed
        clock.tick(snake_speed)
 
    pygame.quit()
    print("Game Terminated.")
    quit()
 
 
gameLoop()