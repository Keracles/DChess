import pygame
import os

import pygame
import os

#Size
Width, Height = 760,760
Rows, Cols = 8,8
Square = Width//Rows

#Colors
Bg = (47,79,79)
Black = (0,0,0)
White = (255,255,255)
beige = (245,245,220)
brown_chocolate = (210,105,30)
brown = (55,55,55)
cornsilk = (255,248,220)
Grey = (201,201,201)

path_image = "DChess\images"

#Black pieces

Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bkn.png")), (Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bb.png")), (Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"br.png")), (Square, Square))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bk.png")), (Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bq.png")), (Square, Square))
Black_Pawn = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"bp.png")), (Square, Square))

#White pieces

White_Knight = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wkn.png")), (Square, Square))
White_Bishop = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wb.png")), (Square, Square))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wr.png")), (Square, Square))
White_King = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wk.png")), (Square, Square))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wq.png")), (Square, Square))
White_Pawn = pygame.transform.scale(pygame.image.load(os.path.join(path_image,"wp.png")), (Square, Square))