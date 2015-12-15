import pygame

# Colours
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mastermind")

def button(x, y, colour):
    pygame.draw.circle(screen, colour, [x, y], 20)

colour = white
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
               colour = blue
            elif event.key == pygame.K_r:
                colour =  red

    screen.fill(white)
    x_start = 100
    button(x_start, 500, red)
    button(x_start + 50, 500, blue)
    button(x_start + 100, 500, green)
    button(x_start + 150, 500, black)
    pygame.display.update()




pygame.quit()

