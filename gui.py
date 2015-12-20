import random
import pygame
from get_indicators import get_indicators
from pygame.locals import MOUSEBUTTONDOWN

# Colours
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(255, 255, 0)
purple = pygame.Color(160, 32, 240)
orange = pygame.Color(255, 165, 0)

colour_choice = [red, blue, yellow, purple, orange]

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Mastermind")
clock = pygame.time.Clock()


class Row(object):

    def __init__(self, guess, create_ind=True):
        self._guess = guess
        if create_ind:
            self._indicator = self.get_indicator()
        else:
            self._indicator = []


    def get_indicator(self):
        return get_indicators(self.guess, board.code)

    @property
    def guess(self):
        return self._guess

    @property
    def indicator(self):
        return self._indicator


class Board(object):

    ind_color = {2:red, 1:black, 0:white}

    def __init__(self):
        self.x_start = 200
        self.y_start = 100
        self._code = self.generate_code()
        self._current_guess = []
        self.rows = []
        self.MAX_GUESS = 4
        self.row_count = 0

    @property
    def code(self):
        return self._code

    @property
    def current_guess(self):
        return self._current_guess

    def generate_code(self):
        """Generates a randon code for the user to guess."""
        return [random.choice(colour_choice) for _ in range(4)]

    def add_guess(self, colour):
        self._current_guess.append(colour)

    def add_row(self):
        self.rows.append(Row(self._current_guess))
        self._current_guess = []
        self.row_count += 1

    def display_rows(self):
        for i, row in enumerate(self.rows):
            self.display_row(row, i)

    def display_row(self, row, count):
        y = self.y_start + count * 50
        for i, colour in enumerate(row.guess, 1):
            x = self.x_start + i * 50
            pygame.draw.circle(screen, colour, [x, y], 20)
        for j, ind in enumerate(row.indicator):
            x = self.x_start + 240 + j * 15
            pygame.draw.circle(screen, Board.ind_color[ind], [x, y], 5)

    def display_current_guess(self):
        self.display_row(Row(self._current_guess, create_ind=False), self.row_count)

    def display_code(self):
        y = 20
        for i, colour in enumerate(self._code, 1):
            x = self.x_start + i * 50
            pygame.draw.circle(screen, colour, [x, y], 20)

    def draw_board(self):
        self.display_code()
        self.display_rows()
        self.display_current_guess()

    def draw_empty_board(self):
        for i in range(0, 8):
            y = self.y_start + i * 50
            for j in range(1, 5):
                x = self.x_start + j * 50
                pygame.draw.circle(screen, black, [x, y], 20)
            for j in range(1, 5):
                x = self.x_start + 240 + j * 15
                pygame.draw.circle(screen, white, [x, y], 5)


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
orange_button = Button(x_start + 200, 500, orange, screen)
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
            elif orange_button.pressed():
                board.add_guess(orange)

        elif event.type == MOUSEBUTTONDOWN and \
                len(board.current_guess) == board.MAX_GUESS:
            if add_row_button.pressed():
                print "add row"
                board.add_row()

    pygame.display.update()
    board.draw_board()

pygame.quit()
