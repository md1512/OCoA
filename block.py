import pygame
class block:
	x=0
	y=0
	life=0
	img=''

def set_pos(self,ex,ey,el):
	self.x=ex
	self.y=ey
	self.life=el

def get_pos(self):
	return (self.x,self.y,self.life)
