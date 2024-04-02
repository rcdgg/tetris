import pygame as pg
from game import Game
from sys import exit
from itertools import cycle
pg.init()
screen = pg.display.set_mode((500,620))
pg.display.set_caption('hello')
clock = pg.time.Clock()
game = Game()
GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE,300)
happy = pg.image.load('images\happy lebaron.png')
happy = pg.transform.scale(happy,(150,150))

evil = pg.image.load('images\evil lebaron.png')
evil = pg.transform.scale(evil,(250,100))

#game over text
GAME_OVER = pg.USEREVENT+1
pg.time.set_timer(GAME_OVER,600)
game_over_text = pg.font.Font('Minecraft.ttf',size = 35)
text_surf = game_over_text.render(
''' Press Any Key 
   to Restart''', True, 'White')
text_rect = text_surf.get_rect(center = (160,200))
no_text_surf = pg.surface.Surface(text_rect.size)
no_text_surf.set_colorkey((0,0,0))
text_blink_surf = cycle([text_surf,no_text_surf])
t_b_s = next(text_blink_surf)

score_text = pg.Font('Minecraft.ttf',20)

score_surf = score_text.render('Score',True,'White')
score_rect = score_surf.get_rect(center = (405,50))
next_surf = score_text.render('Next',True,'White')
next_rect = next_surf.get_rect(center = (405,200))

score_r = pg.Rect(320,70,170,50)
next_r = pg.Rect(320,220,170,140)
img_rect = happy.get_rect(center = (next_r.centerx,next_r.centery + 200))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            if game.game_over:
                game.reset()
                
        if event.type == pg.KEYDOWN:
            pg.mixer.Channel(4).play(pg.mixer.Sound('sounds\move sound.ogg'))
            pg.mixer.Channel(4).set_volume(0.2)
            if event.key in (pg.K_a, pg.K_LEFT) and not game.game_over:
                game.move_left()
            if event.key in (pg.K_RIGHT,pg.K_d) and not game.game_over:
                game.move_right()
            if event.key in (pg.K_DOWN,pg.K_s) and not game.game_over:
                game.move_down()
                game.update_score(0,1)
            if event.key in (pg.K_UP,pg.K_w) and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

        if event.type == GAME_OVER:
            t_b_s = next(text_blink_surf)

    screen.fill((44,44,127))
    screen.blit(score_surf,score_rect)
    screen.blit(next_surf,next_rect)
    
    pg.draw.rect(screen,(132, 150, 202),score_r,0,15)
    pg.draw.rect(screen,(132, 150, 202),next_r,0,15)
    score_number = score_text.render(str(game.score),True,'White')
    score_number_surf = score_number.get_rect(centerx = score_r.centerx,centery = score_r.centery)
    screen.blit(score_number,score_number_surf)
    game.draw(screen)

    if game.game_over == False: screen.blit(happy,img_rect) 
    else:
        screen.blit(t_b_s,text_rect)
        screen.blit(evil,img_rect)
    pg.display.update()
    clock.tick(60)
    
