import pygame as pg
from game import Game
from sys import exit
from itertools import cycle
pg.init()

screen = pg.display.set_mode((300,600))
pg.display.set_caption('hello')
clock = pg.time.Clock()
game = Game()
GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE,300)

#game over text
GAME_OVER = pg.USEREVENT+1
pg.time.set_timer(GAME_OVER,600)
game_over_text = pg.font.Font('Minecraft.ttf',size = 35)
text_surf = game_over_text.render(
''' Press Any Key 
   to Restart''', True, 'White')
text_rect = text_surf.get_rect(center = (150,200))
no_text_surf = pg.surface.Surface(text_rect.size)
no_text_surf.set_colorkey((0,0,0))
text_blink_surf = cycle([text_surf,no_text_surf])
t_b_s = next(text_blink_surf)


while True:
    screen.fill((44,44,127))
    game.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            if game.game_over:
                game.reset()
                
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_a, pg.K_LEFT) and not game.game_over:
                game.move_left()
            if event.key in (pg.K_RIGHT,pg.K_d) and not game.game_over:
                game.move_right()
            if event.key in (pg.K_DOWN,pg.K_s) and not game.game_over:
                game.move_down()
            if event.key in (pg.K_UP,pg.K_w) and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

        if event.type == GAME_OVER:
            t_b_s = next(text_blink_surf)
    if game.game_over:
        #screen.blit(stroke_surf,stroke_rect)
        screen.blit(t_b_s,text_rect)
    # game.move_down()
    # rect = pg.Rect(100,100,100,400)
    # pg.draw.rect(screen,(47, 230, 23),rect)
    pg.display.update()
    clock.tick(60)
    
