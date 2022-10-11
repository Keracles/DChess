import pygame
import os

Width, Height = 760,760
Rows, Cols = 8,8
Square = Width//Rows

Brown = (87,16,16)
White = (255,255,255)

path_image = "DChess\images"

#Black pieces

black_knight = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bkn.png")), (Square, Square))
black_bishop = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bb.png")), (Square, Square))
black_tower = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"br.png")), (Square, Square))
black_king = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bk.png")), (Square, Square))
black_queen = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bq.png")), (Square, Square))
black_pawn = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bp.png")), (Square, Square))

#White pieces

white_knight = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wkn.png")), (Square, Square))
white_bishop = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wb.png")), (Square, Square))
white_tower = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wr.png")), (Square, Square))
white_king = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wk.png")), (Square, Square))
white_queen = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wq.png")), (Square, Square))
white_pawn = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wp.png")), (Square, Square))