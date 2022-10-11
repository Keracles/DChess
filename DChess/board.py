import pygame
from .Pieces import *
from .constants import *

class newBoard:
    def __init__(self, Width, Height, Rows, Cols, Square, Win):
        self.Width = Width
        self.Height = Height 
        self.Rows = Rows
        self.Cols = Cols
        self.Square = Square
        self.Win = Win
        self.Board = []
        self.create_Board()
    
    def create_Board(self):
        for row in range(self.Rows):
            self.Board.append([0 for i in range(self.Cols)])
            
            for col in range(self.Cols):
                pass