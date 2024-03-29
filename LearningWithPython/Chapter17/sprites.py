# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 1/25/2022
# About : Drawing a Queen Sprite
# --------------------------------------------------------------------------

import pygame
import random

# ---------------------------------------------------------------------------
gravity = 0.0001

class QueenSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)
        self.y_velocity = 0
    
    def update(self):
        self.y_velocity += gravity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn
        dist_to_go = target_y - new_y_pos

        if dist_to_go < 0:
            self.y_velocity = -0.65 * self.y_velocity
            new_y_pos = target_y + dist_to_go
        
        self.posn = (x, new_y_pos)

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

# ---------------------------------------------------------------------------

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

    # queens list
    all_sprites = []
    # add the queens to the queen list
    for (column, row) in enumerate(board):
        a_queen = QueenSprite(ball, (column*square_size+ball_offset, \
                                        row*square_size+ball_offset))
        all_sprites.append(a_queen)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        for sprite in all_sprites:
            sprite.update()

        for row in range(n):
            color_index = row % 2
            for column in range(n):
                square = (column*square_size, row*square_size, square_size, square_size)
                surface.fill(colors[color_index], square)
                color_index = (color_index + 1) % 2
        
        # preset queens
        # for (column, row) in enumerate(board):
        #     surface.blit(ball, (column*square_size + ball_offset, row*square_size + ball_offset))
            
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()

    pygame.quit


def main():
    draw_board([0, 5, 3, 1, 6, 4, 2])
    # draw_board([0, 5, 3, 1, 6, 4, 2])
    # draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------

def share_diagonal(x1, y1, x2, y2):
    dis_x = abs(x2 - x1)
    dis_y = abs(y2 - y1)
    return dis_x == dis_y

def column_clashes(p, c):
    for i in range(c):
        if share_diagonal(i, p[i], c, p[c]):
            return True
    return False

def has_clashes(board):
    for column in range(1, len(board)):
        if column_clashes(board, column):
            return True
    return False

def random_guessing():
    import random
    rng = random.Random()

    bd = list(range(8))
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print(f"Found solution {bd} in {tries} tries")
            draw_board(bd)
            tries = 0
            num_found += 1