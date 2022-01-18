# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 1/17/2022
# About : Using pygame to a chess board
# --------------------------------------------------------------------------

import pygame

def draw_board(board):

    pygame.init
    colors = [(255, 0, 0), (0, 0, 0)]

    # n = len(board)
    square_size = 480 // board
    surface_size = board*square_size

    surface = pygame.display.set_mode((surface_size, surface_size))

    for row in range(board):
            color_index = row % 2
            for column in range(board):
                square = (column*square_size, row*square_size, square_size, square_size)
                surface.fill(colors[color_index], square)
                color_index = (color_index + 1) % 2

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        pygame.display.flip()

    pygame.quit


def main():
    draw_board(12)

if __name__ == "__main__":
    main()