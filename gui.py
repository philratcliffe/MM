import pygame
from pygame.locals import MOUSEBUTTONDOWN

# Colours
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(255, 255, 0)
purple = pygame.Color(160, 32, 240)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mastermind")
clock = pygame.time.Clock()

class Row(object):

    def __init__(self, guess):
        self.guess = []
        self.indicator = self.get_indicator()

    def get_indicator(self, guess):
        pass

class Board(object):

    def __init__(self):
        self.x_start = 200
        self.y_start = 50
        self.row_count = 0
        self._current_guess = []
        self.rows = []
        self.MAX_GUESS = 4

    @property
    def current_guess(self):
        return self._current_guess

    def add_guess(self, colour):
        self._current_guess.append(colour)

    def add_row(self):
        self.rows.append(self._current_guess)
        self._current_guess = []
        self.row_count += 1

    def display_rows(self):
        for i, row in enumerate(self.rows):
            self.display_row(row, i)

    def display_row(self, row, count):
        y = self.y_start + count * 50
        for i, colour in enumerate(row, 1):
            x = self.x_start + i * 50
            pygame.draw.circle(screen, colour, [x, y], 20)

    def display_current_guess(self):
        self.display_row(self._current_guess, self.row_count)

    def draw_board(self):
        self.display_rows()
        self.display_current_guess()

    def draw_empty_board(self):
        colour = black
        for i in range(0, 8):
            y = self.y_start + i * 50
            for j in range(1, 5):
                x = self.x_start + j * 50
                pygame.draw.circle(screen, colour, [x, y], 20)

class Button(object):

    def __init__(self, x, y, colour, screen):
        self.x = x
        self.y = y
        pygame.draw.circle(screen, colour, [x, y], 20)

    def pressed(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]:
            if self.x + 20 > cur[0] > self.x - 20:
                if self.y + 20 > cur[1] > self.y - 20:
                    if click[0]:
                        return True

        return False

def button(x, y, colour, board):
    pygame.draw.circle(screen, colour, [x, y], 20)
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0]:
        if x + 20 > cur[0] > x - 20:
            if y + 20 > cur[1] > y - 20:
                if click[0]:
                    board.add_guess(colour)

clock.tick(10)
colour = white
quit_game = False

screen.fill(white)
board = Board()
board.draw_empty_board()
x_start = 100
red_button = Button(x_start, 500, red, screen)
blue_button = Button(x_start + 50, 500, blue, screen)
yellow_button = Button(x_start + 100, 500, yellow, screen)
purple_button = Button(x_start + 150, 500, purple, screen)
add_row_button = Button(x_start + 400, 500, green, screen)

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        elif event.type == MOUSEBUTTONDOWN and \
                len(board.current_guess) < board.MAX_GUESS:
            if red_button.pressed():
                board.add_guess(red)
            elif blue_button.pressed():
                board.add_guess(blue)
            elif yellow_button.pressed():
                board.add_guess(yellow)
            elif purple_button.pressed():
                board.add_guess(purple)

        elif event.type == MOUSEBUTTONDOWN and \
                len(board.current_guess) == board.MAX_GUESS:
            if add_row_button.pressed():
                board.add_row()

    pygame.display.update()
    board.draw_board()

pygame.quit()


