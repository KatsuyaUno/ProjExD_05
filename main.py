import pygame
import sys

img_bg = pygame.image.load("ex05/images/bg.jpg")

bg_y = 0

HEIGHT = 600
WIDTH = 800

def main():
    global bg_y

    pygame.init()
    pygame.display.set_caption("シューティングゲームの背景")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg_y = (bg_y + 1) % 600
        screen.blit(img_bg,[0,bg_y - 600])
        screen.blit(img_bg,[0,bg_y])

        pygame.display.update()
        clock.tick(120)
        
if __name__ == "__main__":
    main()
