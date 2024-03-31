import pygame as pg
from game import Game
import sys
pg.init()

screen = pg.display.set_mode((300,600))
pg.display.set_caption('hello')
clock = pg.time.Clock()
game = Game()
GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE,300)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                game.move_left()
            if event.key == pg.K_RIGHT:
                game.move_right()
            if event.key == pg.K_DOWN:
                game.move_down()
            if event.key == pg.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()
    screen.fill((44,44,127))
    game.draw(screen)
    # game.move_down()
    # rect = pg.Rect(100,100,100,400)
    # pg.draw.rect(screen,(47, 230, 23),rect)
    pg.display.update()
    clock.tick(60)
    
