# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 1/17/2022
# About : Using pygame to a chess board
# --------------------------------------------------------------------------

import pygame

def draw_board(board):

    pygame.init
    colors = [(255, 0, 0), (0, 0, 0)]

    n = len(board)
    square_size = 480 // n
    surface_size = n*square_size

    surface = pygame.display.set_mode((surface_size, surface_size))

    ball_file_path = "D:\Lilac\Coding\Python\LearningWithPython\Chapter17\\smallerBeachBall.png"
    ball = pygame.image.load(ball_file_path)
    ball_offset = (square_size-ball.get_width()) // 2

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        for row in range(n):
            color_index = row % 2
            for column in range(n):
                square = (column*square_size, row*square_size, square_size, square_size)
                surface.fill(colors[color_index], square)
                color_index = (color_index + 1) % 2
            
        for (column, row) in enumerate(board):
            surface.blit(ball, (column*square_size + ball_offset, row*square_size + ball_offset))
            
        pygame.display.flip()

    pygame.quit


def main():
    draw_board([0, 5, 3, 1, 6, 4, 2])
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

if __name__ == "__main__":
    main()