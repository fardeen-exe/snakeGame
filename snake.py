import pygame
import random
pygame.mixer.init()
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
bgimgmain = pygame.image.load("game.jpg")
bgimgmain = pygame.transform.scale(bgimgmain, (screen_width, screen_height)).convert_alpha()
bgimgend= pygame.image.load("over.jpg")
bgimgend = pygame.transform.scale(bgimgend, (screen_width, screen_height)).convert_alpha()
bgimgintro= pygame.image.load("1.jpg")
bgimgintro= pygame.transform.scale(bgimgintro,(screen_width, screen_height)).convert_alpha()
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def screen1(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plotSn(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcomeSc():
    pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play()    
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimgintro, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play()
                    lOOp()

        pygame.display.update()
        clock.tick(60)



def lOOp():
    
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1


    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(bgimgend, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcomeSc()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
            gameWindow.fill(white)
            gameWindow.blit(bgimgmain, (0, 0))
            screen1("Score: " + str(score), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('sound.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('sound.mp3')
                pygame.mixer.music.play()
            plotSn(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcomeSc()
