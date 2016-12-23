import pygame,sys,random
from pygame.locals import *
from numpy import *
from Enemy import Enemy

class Level:
	def __init__(s,data):
		s.data=data
	def initlevel(s):
		s.myshoots=[]
		s.enemyshoots=[]
		s.enemys=[]
		s.data.pl.puntos=0
		s.data.pl.vidas=3
		for x in xrange(1,5):
			x,y,inc,dis=random.randint(0,400),random.randint(100,150),random.randint(10,15),random.randint(3,5)
			s.enemys.append(Enemy(s.data,x,y,inc,dis))

	def render(s):
		pygame.display.set_caption("Nivel")

		if len(s.enemys)==0:
			s.data.status="Ganaste"
			s.data.indexScene=3;

		for shoot in s.myshoots:
			shoot.y-=1
			pygame.draw.rect(s.data.ventana,(100,0,0),shoot)
			if(shoot.y<0):
				s.delMyShoot(shoot)
		for enemy in s.enemys:
			enemy.render()
		for shoote in s.enemyshoots:
			shoote.y+=1
			pygame.draw.rect(s.data.ventana,(100,0,0),shoote)
			if(shoote.y>600):
				s.delEnemyShoot(shoote)

		s.data.mis.createText("Vidas: "+str(s.data.pl.vidas),50,(0,30))
		s.data.mis.createText("Puntos: "+str(s.data.pl.puntos),50,(300,30))


	def delMyShoot(s,it):
		s.myshoots.remove(it)
	def addMyShoot(s,it):
		s.myshoots.append(it)
	def delEnemyShoot(s,it):
		s.enemyshoots.remove(it)
	def addEnemyShoot(s,it):
		s.enemyshoots.append(it)