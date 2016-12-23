import pygame,sys,random
from pygame.locals import *

class Final:
    def __init__(s,data):
        s.data=data
        s.btnJugar=""
        s.btnExit=""
    def render(s):
        pygame.display.set_caption(s.data.status)
        mitadx=s.data.widthWindow/2
        mitady=s.data.heightWindow/2
        s.data.mis.createText(str(s.data.status),100,(mitadx-180,30))
        s.data.mis.createText("Puntos: "+str(s.data.pl.puntos),50,(mitadx-180,150))
        s.btnJugar=s.data.mis.createButton("Reintentar",30,(mitadx-180,mitady-100),(180,50),(220,220,220))
        s.btnExit=s.data.mis.createButton("Inicio",30,(mitadx-180,mitady),(100,50),(220,220,220))

        for event in pygame.event.get():
            if event.type == QUIT or(event.type==KEYDOWN and event.key==K_ESCAPE):
                s.data.closeGame()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if s.btnJugar.collidepoint(pos):
                    s.data.indexScene=2;
                    s.data.lv.initlevel()
                elif s.btnExit.collidepoint(pos):
                    s.data.indexScene=1