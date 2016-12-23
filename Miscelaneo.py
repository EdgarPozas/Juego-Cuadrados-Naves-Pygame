import pygame,sys,random
from pygame.locals import *

class Miscelaneo:
    def __init__(s,data):
        s.data=data
    def createText(s,txt,size,pos):
        s.font_inicial=pygame.font.Font(pygame.font.get_default_font(),size)
        text=s.font_inicial.render(txt,True,(0,0,0));
        s.data.ventana.blit(text, (pos[0], pos[1]))
    def createButton(s,txt,sizeF,pos,sizeB,color):
        var=pygame.Rect(pos[0],pos[1],sizeB[0],sizeB[1])
        pygame.draw.rect(s.data.ventana,color,var)
        s.createText(txt,sizeF,((pos[0]+5, pos[1]+6)))
        return var
