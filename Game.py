import pygame,sys,random
from pygame.locals import *
from Inicial import Inicial
from Levels import Level
from Player import Player
from Enemy import Enemy
from Final import Final

from Miscelaneo import Miscelaneo


WIDTH=800
HEIGHT=700

class Game:
	def __init__(s):
		s.indexScene=1
		pygame.init()
		s.widthWindow=WIDTH
		s.heightWindow=HEIGHT
		s.ventana = pygame.display.set_mode((WIDTH,HEIGHT))
		
		s.mis=Miscelaneo(s)
		
		s.pl=Player(s)
		s.lv=Level(s)
		s.init=Inicial(s)
		s.fin=Final(s)
		s.loopGame()
	def loopGame(s):
		while(True):
			s.ventana.fill((255,255,255))

			if s.indexScene==1:
				s.init.render()
			elif s.indexScene==2:
				s.pl.render()
				s.lv.render()
			elif s.indexScene==3:
				s.fin.render()

			#pygame.time.delay(1)
			pygame.display.flip()
	def closeGame(s):
		sys.exit()

if __name__ == '__main__':
	Game()