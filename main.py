from operator import truediv
import pygame

from DChess.constants import *

pygame.init()

clock = pygame.time.Clock()

Win = pygame.display.set_mode((Width, Height))

def get_position(x,y):
    row = y//Square
    col = x//Square
    return row,col


def main():
    run = True
    FPS = 60
    game_over = False
    while run:
        clock.tick(FPS)
        Win.blit(white_bishop, (50,50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE and game_over:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if pygame.mouse.get_pressed()[0]:
                    location = pygame.mouse.get_pos()
                    row,col = get_position(location[0], location[1])

main()