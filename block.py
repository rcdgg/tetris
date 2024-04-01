from grid import Grid
import pygame as pg
class Block:
    colors = Grid.get_colors()
    def __init__(self,id) -> None:
        self.colors = Block.colors
        self.id = id
        self.r_offset = 0
        self.c_offset = 0
        self.rotation = 0
        self.cell_size = 30
        self.state = {}

    def draw(self,screen):
        block_state = self.block_pos()
        for tile in block_state:
            tile_rect = pg.Rect(tile[1]*self.cell_size +11,tile[0]*self.cell_size+11,self.cell_size -1,self.cell_size-1)
            pg.draw.rect(screen,self.colors[self.id],tile_rect)

    def move(self,row,col):
        self.r_offset += row
        self.c_offset += col

    def block_pos(self):
        block = self.state[self.rotation]
        return [(i+self.r_offset,j+self.c_offset) for (i,j) in block]
    
    def rotate(self):
        self.rotation = (self.rotation +1)%len(self.state)
    def unrotate(self):
        self.rotation = (self.rotation -1)%len(self.state)


class Jblock(Block):
    def __init__(self) -> None:
        super().__init__(id = 1)
        self.state = {
            0: [(0,0),(1,0),(1,1),(1,2)],
            1: [(0,1),(0,2),(1,1),(2,1)],
            2: [(1,0),(1,1),(1,2),(2,2)],
            3: [(0,1),(1,1),(2,1),(2,0)]
        }
        self.move(0,3)
    
class Lblock(Block):
    def __init__(self) -> None:
        super().__init__(id = 2)
        self.state = {
            0: [(0,1),(1,1),(2,1),(2,2)],
            1: [(1,1),(1,2),(1,0),(2,0)],
            2: [(2,1),(0,1),(1,1),(0,0)],
            3: [(1,1),(1,0),(1,2),(0,2)]
        }
        self.move(0,3)

class Oblock(Block):
    def __init__(self) -> None:
        super().__init__(id = 3)
        self.state = {
            0: [(0,0),(1,0),(1,1),(0,1)]
        }
        self.move(0,4)

class Tblock(Block):
    def __init__(self) -> None:
        super().__init__(id = 4)
        self.state = {
            0: [(0,0),(0,1),(1,1),(0,2)],
            1: [(0,2),(1,2),(1,1),(2,2)],
            2: [(2,0),(1,1),(2,2),(2,1)],
            3: [(0,0),(1,1),(1,0),(2,0)]
        }
        self.move(0,3)

class Iblock(Block):
    def __init__(self) -> None:
        super().__init__(id = 5)
        self.state = {
            0: [(1,2),(1,1),(1,3),(1,0)],
            1: [(0,1),(1,1),(2,1),(3,1)],
        }
        self.move(-1,3)

class Zblock(Block):
    def __init__(self) -> None:
        super().__init__(id = 6)
        self.state = {
            0: [(0,0),(0,1),(1,1),(1,2)],
            1: [(0,2),(1,2),(1,1),(2,1)],
        }
        self.move(0,3)

class Sblock(Block):
    def __init__(self) -> None:
        super().__init__(id = 7)
        self.state = {
            0: [(0,2),(0,1),(1,1),(1,0)],
            1: [(0,1),(1,2),(1,1),(2,2)],
        }
        self.move(0,3)


