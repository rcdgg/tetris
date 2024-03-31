from grid import Grid
from block import *
import random

class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = [Tblock(),Sblock(),Zblock(),Iblock(),Oblock(),Jblock(),Lblock()]
        self.curr_block = self.get_block()
        self.next_block = self.get_block()

    def get_block(self):
        if self.blocks == []:
            self.blocks = [Tblock(),Sblock(),Zblock(),Iblock(),Oblock(),Jblock(),Lblock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.curr_block.move(0,-1)
        if not self.in_bound() or not self.valid():
            self.curr_block.move(0,1)

    def move_right(self):
        self.curr_block.move(0,1)
        if not self.in_bound() or not self.valid():
            self.curr_block.move(0,-1)

    def move_down(self):
        self.curr_block.move(1,0)
        if not self.in_bound() or not self.valid():
            self.curr_block.move(-1,0)
            self.lock()

    def lock(self):
        tiles = self.curr_block.block_pos()
        for tile in tiles:
            self.grid.grid[tile[0]][tile[1]] = self.curr_block.id
        self.curr_block = self.next_block
        self.next_block = self.get_block()

    def valid(self):
        tiles= self.curr_block.block_pos()
        for tile in tiles:
            if self.grid.empty(tile[0],tile[1]) == False:
                return False
        return True

    def rotate(self):
        self.curr_block.rotate()
        if self.in_bound() == False or not self.valid(): 
            self.curr_block.unrotate()

    def in_bound(self):
        tiles = self.curr_block.block_pos()
        for tile in tiles:
            if self.grid.inside(tile[0],tile[1]) == False:
                return False
        return True

    def draw(self,screen):
        self.grid.draw(screen)  
        self.curr_block.draw(screen)