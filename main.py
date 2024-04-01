import pygame as pg
from game import Game
import sys
pg.init()

screen = pg.display.set_mode((300,600))
pg.display.set_caption('hello')
clock = pg.time.Clock()
game = Game()
GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE,20)
game_over_text = pg.font.Font(None,size = 40)
text_surf = game_over_text.render(
'''Press Any Key 
   to Restart''', False, 'White')
text_rect = text_surf.get_rect(center = (150,150))
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if game.game_over:
                game.reset()
                
            if event.key == pg.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pg.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pg.K_DOWN and not game.game_over:
                game.move_down()
            if event.key == pg.K_UP and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()
    screen.fill((44,44,127))
    game.draw(screen)
    if game.game_over:
        screen.blit(text_surf,text_rect)
    # game.move_down()
    # rect = pg.Rect(100,100,100,400)
    # pg.draw.rect(screen,(47, 230, 23),rect)
    pg.display.update()
    clock.tick(60)
    
