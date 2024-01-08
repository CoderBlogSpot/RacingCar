import pygame
import time
import random
pygame.init()

# Global Constants
FPS = 60
WIDTH = 800
HEIGHT = 600

# Global Variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RacingCar!!!!")
clock = pygame.time.Clock()

# Define some Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
block_color = (53, 115, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# Load Images
car_img = pygame.image.load("assets/images/racecar.png")

# More variables
car_width = 73

# Functions
def dodge(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    screen.blit(text, (0, 0))


def things(thing_x, thing_y, width, height, color):
    pygame.draw.rect(screen, color, [thing_x, thing_y, width, height])

def car(x, y):
    screen.blit(car_img, (x, y))

def text_obj(txt, font):
    surface = font.render(txt, True, black)
    return surface, surface.get_rect()

def msg_display(txt):
    large_txt = pygame.font.SysFont("freesansbold.ttf", 115)
    txtsurface, txtrect = text_obj(txt, large_txt)
    txtrect.center = ((WIDTH/2), (HEIGHT/2))
    screen.blit(txtsurface, txtrect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    msg_display("You crashed!!!")
    pygame.quit()
    quit()

# Main game loop
def game_loop():
    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.8)
    x_change = 0

    thing_start_x = random.randrange(0, WIDTH)
    thing_start_y = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    things_count = 1
    dodged = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change    
        screen.fill(white)
        
        things(thing_start_x, thing_start_y, thing_width, thing_height, block_color)
        thing_start_y += thing_speed
        car(x, y)
        dodge(dodged)

        if x > WIDTH - car_width or x < 0:
            crash()

        if thing_start_y > WIDTH:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, WIDTH)
            dodge += 1
            thing_speed += 1
            thing_width += (dodge * 1.2)
        
        if y < thing_start_y + thing_height:
            print("y crossover")
            if x > thing_start_x and x < thing_start_x + thing_width or x + car_width > thing_start_x and x + car_width < thing_start_x + thing_width:
                print("x crossover")
                crash()

        pygame.display.update()
        clock.tick(FPS)

game_loop()
pygame.quit()
quit()