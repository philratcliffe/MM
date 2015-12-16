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
clock = pygame.time.Clock()

class Guess(object):

    def __init__(self):
        self.guess = []

    def add_colour(self, colour):
        self.guess.append(colour)

    def get_guess(self):
        return self.guess

class Board(object):

    def __init__(self):
        self.x_start = 200
        self.y_start = 50
        self.row_count = 0
        self.current_guess = []
        self.rows = []

    def add_guess(self, colour):
        self.current_guess.append(colour)

    def add_row(self):
        self.rows.append(self.current_guess)
        self.current_guess = []
        self.row_count += 1

    def display_rows(self):
        for i, row in self.rows:
            self.display_row(row, i)

    def display_row(self, row, count):
        y = self.y_start + count * 50
        for i, colour in enumerate(row):
            x = self.x_start + i * 50
            pygame.draw.circle(screen, colour, [x, y], 20)

    def display_current_guess(self):
        self.display_row(self.current_guess, self.row_count)

    def draw_board(self):
        self.display_rows()
        self.display_current_guess()

    def draw_empty_board(self):
        colour = black
        for i in range(1, 8):
            y = self.y_start + i * 50
            for j in range(1, 5):
                x = self.x_start + j * 50
                pygame.draw.circle(screen, colour, [x, y], 20)

class Button(object):

    def __init__(x, y, colour, screen):
        pygame.draw.circle(screen, colour, [x, y], 20)


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
x_start = 100
button(x_start, 500, red, board)
button(x_start + 50, 500, blue, board)
button(x_start + 100, 500, green, board)
button(x_start + 150, 500, red, board)
button(x_start + 150, 500, black, board)


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    board.draw_empty_board()
    board.draw_board()


    pygame.display.update()

pygame.quit()

