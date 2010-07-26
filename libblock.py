class block:
	x=0
	y=0
	life=0
	img=''

def init__(self,x,y,life,img):
	self.x=x
	self.y=y
	self.life=life
	self.img=img

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
