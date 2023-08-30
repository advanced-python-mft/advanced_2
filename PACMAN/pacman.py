# library
import pygame as pg
from maps import MAP 
import time
import sys
import math
# init pygame 
pg.init()
width_screen=550
height_screen=800
# screen meno
screen=pg.display.set_mode((height_screen,width_screen+50))
pg.display.set_caption('<<PAC|MAN>>')
icon=pg.image.load('pics/pacman_icon.jpg')
pg.display.set_icon(icon)
circle_smale=0
color_circle=(255,255,255)
def draw_meno():
    screen.fill((0,0,25))
    pg.draw.circle(screen,(2,100,160),(390,300),100)
    pg.draw.rect(screen,(7,110,169),(220,430,345,150))
    font_style = pg.font.SysFont(None, 69)
    font_style2 = pg.font.SysFont(None, 69)
    font_style3 = pg.font.SysFont(None, 110)
    m=font_style.set_underline(True)
    mesg = font_style.render('Start', True, (255,255,255))
    name_mesg = font_style2.render('<< PACMAN >>', True, (255,255,255))
    nd1 = font_style3.render('>  >  >', True, (255,255,255))
    nd2 = font_style3.render('<  <  <', True, (255,255,255))
    pac=pg.image.load('pics/pacman_meno.jpg')
    aa=pg.image.load('pics/AA.jpg')
    pac2=pg.image.load('pics/pacman_meno2.jpg')
    shabah=pg.image.load('pics/shabah_mano.jpg')
    shabah2=pg.image.load('pics/shabah_mano2.jpg')
    screen.blit(mesg,[340,280])
    screen.blit(nd1,[550,260])
    screen.blit(nd2,[30,260])
    screen.blit(name_mesg,[220,480])
    screen.blit(pac,[30,500])
    screen.blit(pac2,[700,500])
    screen.blit(aa,[374,5])
    screen.blit(shabah,[30,20])
    screen.blit(shabah2,[700,20])
    screen.blit(shabah,[220,100])
    screen.blit(shabah2,[500,100])
x=True
snd = pg. mixer. Sound('music/music_meno.mp3')
snd. play()
while x:
    draw_meno()
    for event in pg.event.get():
        #turn off
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.type == pg.KMOD_ALT:
                    x=False
    pg.display.update()
snd.stop()           
# screen game
screen=pg.display.set_mode([height_screen-100,width_screen+75])
pg.display.set_caption('<<PAC|MAN>>')
icon=pg.image.load('pics/pacman_icon.jpg')
pg.display.set_icon(icon)
# Game_map
def draw_map():
    global circle_smale
    global color_circle
    for index_x,line in enumerate(MAP):
        for index_y,colon in enumerate(line):
            width=width_screen//len(line)
            height=height_screen//len(MAP)
            if colon == 1:
                circle_smale=pg.draw.circle(screen,(color_circle),((index_y*height)+(height * 0.5),(index_x * width)+(width * 0.5)),2)
            elif colon == 2:
                pg.draw.circle(screen,(230,210,50),((index_y*height)+(height * 0.5),(index_x * width)+(width * 0.5)),6)
            elif colon == 3:
                pg.draw.line(
                    surface=screen,
                    color=(255,255,255),
                    start_pos=(
                        (index_y*height) + (height * 0.5),
                        index_x*width+ height
                    ),
                    end_pos=(
                        (index_y*height) + (height * 0.5),
                        index_x * width
                    ),
                    width=3
                )
            elif colon == 4:
                pg.draw.line(
                    surface=screen,
                    color=(0,100,200),
                    start_pos=(
                        index_y*height ,
                        (index_x * width) + (width * 0.5)
                    ),
                    end_pos=(
                        (index_y*height) +   height,
                        (index_x * width) + (width * 0.5)
                    ),
                    width=3
                )   
            elif colon == 5:
                pg.draw.arc(
                    screen,
                    (10,200,180),
                    [
                        (index_y * height-(height * 0.4))-2,
                        (index_x*width+(0.5*width)),
                        height,
                        width
                    ],
                    0,
                    math.pi/2,
                    3
                )
            elif colon == 6:
                pg.draw.arc(
                    screen,
                    (250,250,250),
                    [
                        index_y * height + (height * 0.5),
                        index_x * width + (width * 0.5),
                        height,
                        width
                    ],
                    math.pi/2,
                    math.pi,
                    3
                )
            elif colon == 7:
                pg.draw.arc(
                    surface=screen,
                    color=(0,100,200),
                    rect=[
                        (index_y*height+(height*.5)),
                        (index_x*width-(.4 * width)),
                        height,
                        width
                    ],
                    start_angle=math.pi,
                    stop_angle=3 * math.pi / 2,
                    width=3
                )
            elif colon == 8:
                pg.draw.arc(
                    surface=screen,
                    color=(0,0,100),
                    rect=[
                        (index_y*height-(height*.4)) -2,
                        (index_x*width-(.4 * width)),
                        height,
                        width
                    ],
                    start_angle=3 * math.pi / 2,
                    stop_angle=2 * math.pi,
                    width=3
                )
            elif colon ==9:
                pg.draw.line(
                    surface=screen,
                    color=(250,250,0),
                    start_pos=(
                        index_y*height ,
                        (index_x * width) + (width * 0.5)
                    ),
                    end_pos=(
                        (index_y*height) +   height,
                        (index_x * width) + (width * 0.5)
                    ),
                    width=3
                )             
# enemy
player=pg.image.load('pics/pacman_R.jpg')
shabah=pg.image.load('pics/shabah.jpg')
shabah2=pg.image.load('pics/shabah 2.jpg')
shabah3=pg.image.load('pics/shabah3.jpg')
X, y = 60, 50
x_change = 0
y_change = 0
clock = pg.time.Clock()
x=True
# gameloop
time_game=0
time_game_big=0
scor=0
while x:
    time_game+=1
    if time_game == 99999999999999999999:
        time_game_big+=1
        time_game-=99999999999999999999
    if time_game_big==999999999999:
        scor+=10
        time_game_big-=999999999999
    clock.tick(10)
    for event in pg.event.get():
        #turn off
        if event.type == pg.QUIT:
            x=False
        # keybord
        if event.type == pg.KEYDOWN:
            snd = pg. mixer. Sound('music/pacman_music.mp3')
            snd. play()
            if event.key == pg.K_RIGHT:
                player=pg.image.load('pics/pacman_R.jpg')
                x_change = 10
                y_change = 0
            elif event.key == pg.K_LEFT:
                player=pg.image.load('pics/pacman_L.jpg')
                x_change = -10
                y_change = 0
            elif event.key == pg.K_UP:
                player=pg.image.load('pics/pacman_U.jpg')
                x_change = 0
                y_change = -10
            elif event.key == pg.K_DOWN:
                player=pg.image.load('pics/pacman_D.jpg')
                x_change = 0
                y_change =10
            
    # location
    o3=20
    o2=0
    o1=0
    screen.fill((o1,o2,o3))
    draw_map()
    o2+=100
    X += x_change
    y += y_change
    if x<0:
        X = height_screen
    xs=330
    ys=280
    screen.blit(player,[X,y])
    screen.blit(shabah,[xs,ys])
    screen.blit(shabah2,[xs+40,ys])
    screen.blit(shabah3,[xs-40,ys]) 



    # SCORE,time
    font_style=pg.font.SysFont(None,20)
    mesg = font_style.render(f'time:{time_game}', True, (200,255,230))
    mesg2 = font_style.render(f'score:{scor}', True, (200,200,100))
    mesg3 = font_style.render(f'big time:{time_game_big}', True, (200,200,250))
    screen.blit(mesg3,(240,5))
    screen.blit(mesg,(40,5))
    screen.blit(mesg2,(400,5))
    pg.display.update()
    clock.tick_busy_loop(30)
    if y>= width_screen or X>=(height_screen-160):
        x=False
    if y<=30 or X<=20:
        x=False
    if x==False:
        # gameover_screen
        snd = pg. mixer. Sound('music/music_gameove.mp3')
        snd. play()
        time.sleep(0.5)
        font_style = pg.font.SysFont(None, 100)
        mesg = font_style.render('! game ovre !', True, (200,3,0))
        screen.fill((20,0,0))
        screen.blit(mesg,[100, 300])
        pg.display.update()
        time.sleep(1)
pg.display.update()
# get out
pg.quit()
sys.exit()

