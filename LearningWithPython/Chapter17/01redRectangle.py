# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 1/15/2022
# About : Using pygame to create a red rectangle
# --------------------------------------------------------------------------

import pygame

def main():
    # print("Red Rectangle")
    pygame.init()
    
    board_size = (480, 480)
    game_board = pygame.display.set_mode(board_size)

    rectangle_dim = (300, 200, 150, 90)
    red_hue = (255, 0, 0)
    board_hue = (0, 200, 255)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # coloring board game
        game_board.fill(board_hue)
        game_board.fill(red_hue, rectangle_dim)
        
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()