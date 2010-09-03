import pygame
class block:
	x=0
	y=0
	life=0
	img=''
	imgsr=pygame.Surface((0,0))
	rect=pygame.Rect(0,0,0,0)

##def init__(self,x,y,life,img):
##	self.x=x
##	self.y=y
##	self.life=life
##	self.img=img
##	createrect(self)

def set_pos(self,ex,ey,el):
	self.x=ex
	self.y=ey
	self.life=el

def get_pos(self):
	return (self.x,self.y,self.life)
def set_img(self,image):
	self.img=image
def get_img(self):
	return (self.img)
def get_all(self):
	return (self.x,self.y,self.life,self.img)
def createrect(self):
	self.imgsr=pygame.image.load(self.img).convert()
	self.rect=self.imgsr.get_rect()
	self.rect.top=self.y
	self.rect.left=self.x
	
