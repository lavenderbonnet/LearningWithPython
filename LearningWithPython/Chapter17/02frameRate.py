import pygame
import time


#----------------------------------------
def main():
    
    pygame.init()

    board_dims = (1000, 1000)
    game_board = pygame.display.set_mode(board_dims)
    game_font = pygame.font.SysFont("Courier", 50)
    game_board_hue = (0,200,255)
 
    ball_file_path = "D:\Lilac\Coding\Python\LearningWithPython\Chapter17\\beachBall.png"
    ball = pygame.image.load(ball_file_path)
    ball_dims = (100,120)

    banner_dims = (10,10)
    banner_hue = (0,0,0)

    frame_count = 0
    frame_rate = 0
    t0 = time.time()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        frame_count += 1
        if frame_count %500 == 0 :
            t1 = time.time()
            frame_rate = 500/(t1-t0)
            t0 = t1

        game_board.fill(game_board_hue)
        game_board.blit(ball, ball_dims)
        
        banner_text = f"Frame={frame_count}, rate={frame_rate:1.2f}"
        # banner_text = f"Frame={frame_count}"
        banner = game_font.render(banner_text, True, banner_hue )
        game_board.blit(banner, banner_dims)

        pygame.display.flip()

    pygame.quit()

#----------------------------------------


if __name__ == "__main__":
    main()