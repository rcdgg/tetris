import pygame as pg

class Grid:
    def __init__(self) -> None:
        self.cols = 10
        self.rows = 20
        self.grid = [[0 for i in range( self.cols)] for j in range(self.rows)]
        self.colors = self.get_colors()
        self.cell_size = 30
    @staticmethod
    def get_colors():
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple=(166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        return [dark_grey,green,red,orange,yellow,purple,cyan,blue]
    
    def disp_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.grid[i][j], end = " ")
            print()

    def draw(self,screen):
        for i in range(self.rows):
            for j in range(self.cols):
                cell_val = self.grid[i][j]
                cell_rect = pg.Rect(j*self.cell_size+1,i*self.cell_size+1,self.cell_size-1,self.cell_size-1)
                pg.draw.rect(screen,self.colors[cell_val],cell_rect)

    def inside(self,row,col):
        if (0 <= row < self.rows) and( 0<= col < self.cols):
            return True
        return False
    
    def empty(self,row,col):
        if self.grid[row][col] == 0: return True
        return False
    def is_row_full(self,row):
        for col in range(self.cols):
            if self.grid[row][col] == 0: return False
        return True
    def empty_row(self,row):
        for col in range(self.cols):
            self.grid[row][col] = 0
    def move_row(self,row,k):
        if k!= 0:
            for col in range(self.cols):
                self.grid[row+k][col] = self.grid[row][col]
    def clear_row(self):
        complete = 0
        for row in range(self.rows-1,0,-1):
            if self.is_row_full(row):
                complete +=1
            else:
                self.move_row(row,complete)

    def reset(self):
        self.grid = [[0 for i in range( self.cols)] for j in range(self.rows)]