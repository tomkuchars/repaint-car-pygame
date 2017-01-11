import pygame
import time
import random
#import os
#import gtk

#screen_width = gtk.gdk.screen_width()
#screen_height = gtk.gdk.screen_height()

pygame.init()

display_width = 534
display_height = 726

#pos_x = screen_width / 2 - display_width / 2
#pos_y = screen_height - display_height
#os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
#os.environ['SDL_VIDEO_CENTERED'] = '0'

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Przemaluj auto')
clock = pygame.time.Clock()

carImg=[]
carImg.append(pygame.image.load('samochodzik60x132czerwony.png'))
carImg.append(pygame.image.load('samochodzik60x132czarny.png'))
carImg.append(pygame.image.load('samochodzik60x132brazowy.png'))
carImg.append(pygame.image.load('samochodzik60x132fioletowy.png'))
carImg.append(pygame.image.load('samochodzik60x132morski.png'))
carImg.append(pygame.image.load('samochodzik60x132niebieski.png'))
carImg.append(pygame.image.load('samochodzik60x132pomaranczowy.png'))
carImg.append(pygame.image.load('samochodzik60x132rozowy.png'))
carImg.append(pygame.image.load('samochodzik60x132zielony.png'))
carImg.append(pygame.image.load('samochodzik60x132zolty.png'))
carImgRev=[]
carImgRev.append(pygame.image.load('samochodzik60x132czerwonyRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132czarnyRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132brazowyRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132fioletowyRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132morskiRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132niebieskiRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132pomaranczowyRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132rozowyRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132zielonyRev.png'))
carImgRev.append(pygame.image.load('samochodzik60x132zoltyRev.png'))
brushImg=[]
brushImg.append(pygame.image.load('pedzelek60x132czerwony.png'))
brushImg.append(pygame.image.load('pedzelek60x132czarny.png'))
brushImg.append(pygame.image.load('pedzelek60x132brazowy.png'))
brushImg.append(pygame.image.load('pedzelek60x132fioletowy.png'))
brushImg.append(pygame.image.load('pedzelek60x132morski.png'))
brushImg.append(pygame.image.load('pedzelek60x132niebieski.png'))
brushImg.append(pygame.image.load('pedzelek60x132pomaranczowy.png'))
brushImg.append(pygame.image.load('pedzelek60x132rozowy.png'))
brushImg.append(pygame.image.load('pedzelek60x132zielony.png'))
brushImg.append(pygame.image.load('pedzelek60x132zolty.png'))

backImg = pygame.image.load('tlo2.png')
car_width = 60
car_height = 132
brush_width = 60
brush_height = 132
back_width = 534
back_height = 1452
back_height_small = 1452/6

def cars_painted(count):
    font = pygame.font.Font('freesansbold.ttf',72)
    # font = pygame.font.SysFont(None, 72)
    # text = font.render("Przemalowane: "+str(count), True, black)
    text = font.render(str(count), True, black)
    gameDisplay.blit(text,(5,5))

def draw(carImg,x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',72)
    # largeText = pygame.font.SysFont(None, 72)
    TextSurf, TextRect = text_objects(text, largeText, black)
    TextRect.center = (display_width/2,display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def crash():
    message_display('Wypadek!')
    game_loop()

def game_loop():

    level = 1

    x = ((display_width - car_width)* 0.5)
    y = (display_height - car_height) #- 5

    x_change = 0

    car_startx = random.randrange(0, display_width-car_width)
    car_starty = -car_height

    brush_startx = random.randrange(0, display_width-brush_width)
    brush_starty = -brush_height

    back_startx = 0
    back_starty = display_height - back_height

    actualCarImgNr = random.randrange(0, 10)
    actualCarImgRevNr = random.randrange(0, 10)

    newBrushImgNr = random.randrange(0, 10)
    while actualCarImgNr == newBrushImgNr:
        newBrushImgNr = random.randrange(0, 10)
    actualBrushImgNr = newBrushImgNr

    paintedNr = 0
    painted = False

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # print(event)

            if pygame.key.get_pressed()[pygame.K_LEFT] != 0 :
                x_change = -level*2

            if pygame.key.get_pressed()[pygame.K_RIGHT] != 0 :
                x_change = level*2

            if( pygame.key.get_pressed()[pygame.K_LEFT] != 0 and pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ) or ( pygame.key.get_pressed()[pygame.K_LEFT] == 0 and pygame.key.get_pressed()[pygame.K_RIGHT] == 0 ):
                x_change = 0

        x += x_change

        car_speed = level*3
        brush_speed = level*2
        back_speed = level*2

        # gameDisplay.fill(white)

        draw(backImg,back_startx,back_starty)
        back_starty += back_speed

        draw(brushImg[actualBrushImgNr],brush_startx,brush_starty)
        brush_starty += brush_speed

        draw(carImgRev[actualCarImgRevNr],car_startx,car_starty)
        car_starty += car_speed

        draw(carImg[actualCarImgNr],x,y)

        cars_painted(paintedNr)

        if back_starty > -back_height_small:
            back_starty -= 2*back_height_small

        if x < 0 or x > display_width - car_width :
            crash()

        if car_starty > display_height:
            car_startx = random.randrange(0, display_width-car_width)
            car_starty = -car_height
            actualCarImgRevNr = random.randrange(0, 10)

        if brush_starty+brush_height-brush_speed>y and (x < brush_startx+brush_width and x+car_width > brush_startx):
            actualCarImgNr = actualBrushImgNr
            painted = True

        if brush_starty > display_height:
            brush_startx = random.randrange(0, display_width-brush_width)
            brush_starty = -brush_height
            newBrushImgNr = random.randrange(0, 10)
            while actualCarImgNr == newBrushImgNr:
                newBrushImgNr = random.randrange(0, 10)
            actualBrushImgNr = newBrushImgNr
            if painted == True:
                paintedNr += 1
                painted = False
                level += 0.2

        if car_starty+car_height-car_speed>y and (x < car_startx+car_width and x+car_width > car_startx):
            crash()

        pygame.display.update()
        # pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
