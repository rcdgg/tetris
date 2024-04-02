from grid import Grid
from block import *
import random
pg.mixer.init()


class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = [Tblock(),Sblock(),Zblock(),Iblock(),Oblock(),Jblock(),Lblock()]
        self.curr_block = self.get_block()
        self.next_block = self.get_block()
        self.game_over = False
        self.score = 0
        pg.mixer.Channel(0).play(pg.mixer.Sound('sounds\lebaron happy.ogg'),-1)
        pg.mixer.Channel(0).set_volume(0.2)

    def update_score(self,complete_lines,move_down):
        if complete_lines == 0:
            pass
        elif complete_lines == 1:
            self.score += 100
        elif complete_lines == 2:
            self.score += 300
        else:
            self.score += 500
        self.score += move_down

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
        cleared_lines = self.grid.clear_row()
        if self.valid() == False:
            self.game_over = True
            pg.mixer.Channel(0).pause()
            pg.mixer.Channel(1).play(pg.mixer.Sound('sounds\lebaron evil.ogg'),-1)
        self.update_score(cleared_lines,0)

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
        self.curr_block.draw(screen,11,11)
        if self.next_block.id == 2:
            self.next_block.draw(screen,260,240)
        elif self.next_block.id == 3:
            self.next_block.draw(screen,255,260)
        elif self.next_block.id == 5:
            self.next_block.draw(screen,255,270)
        else:
            self.next_block.draw(screen,270,260)

    def reset(self):
        self.grid.reset()
        self.blocks = [Tblock(),Sblock(),Zblock(),Iblock(),Oblock(),Jblock(),Lblock()]
        self.curr_block = self.get_block()
        self.next_block = self.get_block()
        self.game_over = False
        self.score = 0
        pg.mixer.Channel(0).play(pg.mixer.Sound('sounds\lebaron happy.ogg'),-1)
        pg.mixer.Channel(0).set_volume(0.2)
        pg.mixer.Channel(1).pause()