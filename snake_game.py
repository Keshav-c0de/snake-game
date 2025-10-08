import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
red = (213, 50, 80)
orange = (255, 165, 0)
green = (0, 255, 0)
white = (255, 255, 255)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game')

clock = pygame.time.Clock()

snake_size = 10 
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu',25)
score_font = pygame.font.SysFont('ubuntu',20)

def print_score(score):
    text = score_font.render('score: '+ str(score), True , orange)
    game_display.blit(text,[0,0])

def drew_snakes(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0],pixel[1],snake_size,snake_size])


def game_loop():
    game_over = False
    game_close = False 

    x = width /2
    y = height /2

    x_speed = 0
    y_speed = 0

    snake_pixel = []
    snake_lenght = 1

    target_x = round(random.randrange(0,width-snake_size)/10.0)*10.0
    target_y = round(random.randrange(0,height-snake_size)/10.0)*10.0

    while not game_over:
        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render('GAME OVER!',True,red)
            msg2 = message_font.render('Press 1: Quit', True, white)
            msg3 = message_font.render('Press 2: Play Again', True, white)
            game_display.blit(game_over_message,[width / 2 - game_over_message.get_width() / 2, height / 3])
            game_display.blit(msg2, [width / 2 - msg2.get_width() / 2, height / 3 + 40])
            game_display.blit(msg3, [width / 2 - msg3.get_width() / 2, height / 3 + 70])
            print_score(snake_lenght-1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over= True
                        game_close= False
                    if event.key == pygame.K_2:
                        return
                if event.type == pygame.QUIT:
                    game_over= True
                    game_close= False
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange ,[target_x,target_y,snake_size,snake_size])

        snake_pixel.append([x,y])

        if len(snake_pixel)> snake_lenght:
            del snake_pixel[0]

        for pixel in snake_pixel[:-1]:
            if pixel == [x,y]:
                game_close = True

        drew_snakes(snake_size, snake_pixel)
        print_score(snake_lenght - 1)
                
        pygame.display.update()


        if x == target_x and y== target_y:
            target_x = round(random.randrange(0,width-snake_size)/10.0)*10.0
            target_y = round(random.randrange(0,height-snake_size)/10.0)*10.0
            snake_lenght+=1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

def main():
    while True:
        game_loop()

main()

