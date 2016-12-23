import pygame,sys,random
from pygame.locals import *
from numpy import *

class Enemy:
	def __init__(s,data,x,y,inc,dis):
		s.data=data
		s.inc=inc
		s.x,s.y=x,y
		s.enemyRect=""
		s.vidas=3
		s.cont=0
		s.conttimedisparar=0
		s.timedisparar=dis
		s.color=(100,0,0)
	def upLife(s):
		s.vidas+=1
	def downLife(s):
		s.vidas-=1
	def render(s):
		if s.vidas==3:
			s.color=(0,0,255)
		elif s.vidas==2:
			s.color=(0,255,0)
		elif s.vidas==1:
			s.color=(255,0,0)

		for myshoot in s.data.lv.myshoots:
			if s.enemyRect.colliderect(myshoot):
				s.data.lv.myshoots.remove(myshoot)
				s.vidas-=1
		if s.cont<s.inc:
			s.x+=1
		elif s.cont >s.inc:
			s.x-=1
		if s.cont >s.inc*2:
			s.cont=0
		if int(s.conttimedisparar)==s.timedisparar:
			s.data.lv.addEnemyShoot(pygame.Rect(s.x,s.y,5,5))
			s.conttimedisparar=0
		s.enemyRect=pygame.Rect(s.x,s.y,100,100)
		pygame.draw.rect(s.data.ventana,s.color,s.enemyRect)
		s.cont+=0.05
		s.conttimedisparar+=0.01
		if s.vidas <0:
			s.data.pl.puntos+=100
			s.data.lv.enemys.remove(s)
	