import pygame,sys,random
from pygame.locals import *
from numpy import *

class Player:
	def __init__(s,data):
		s.data=data
		s.playerRect=""
		s.vidas=3
		s.puntos=0
		s.x,s.y=600,600
	def addShoot(s):
		s.data.lv.addMyShoot(pygame.Rect(s.x+15,s.y,5,5))
	def move(s,x,y):
 		s.x+=x
 		s.y-=y
	def render(s):
		for event in pygame.event.get():
			if event.type == QUIT or(event.type==KEYDOWN and event.key==K_ESCAPE):
				s.data.closeGame()
				return
			if event.type==KEYDOWN:
				if event.key==K_UP:
					s.cont=pygame.time
					s.move(0,20)
				if event.key==K_DOWN:
					s.move(0,-20)
				if event.key==K_LEFT:
					s.move(-20,0)
				if event.key==K_RIGHT:
					s.move(20,0)
				if event.key==K_SPACE:
					s.addShoot()	
		for enemyshoot in s.data.lv.enemyshoots:
			if s.playerRect.colliderect(enemyshoot):
				s.data.lv.enemyshoots.remove(enemyshoot)
				s.color=(10,10,10)
				s.vidas-=1
		if s.vidas <1:
			s.data.status="Perdiste"
			s.data.indexScene=3;
		s.playerRect=pygame.Rect(s.x,s.y,30,30)
		pygame.draw.rect(s.data.ventana,(100,100,100),s.playerRect)