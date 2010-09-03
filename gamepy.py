#!/usr/bin/python
import sys,time,random
from libblock import *
import pygame,pygame.font,pygame.surface
from configuration import *


pygame.init()
pygame.font.init
fontolo=pygame.font.Font(None, 25)
life=3
rebound=0
point=0
lrebound=0  #last rebound which hit a block
screen = pygame.display.set_caption('OCoA')
screen = pygame.display.set_mode(size)
back = pygame.image.load("background.png").convert()
ball = pygame.image.load("ball.png")#Se necessita' della trasparenza non si deve convertire 
base = pygame.image.load("base.png").convert()
baserect = base.get_rect()
ballrect = ball.get_rect()
backrect= back.get_rect()
baserect.bottom=height-10
baserect.right=(width)/2+40
blocks=[]
lastf=time.time()
for i in range(0,width/lnblock):
	blocks.append(block())
	set_pos(blocks[i],i*(width/10)+(width/10-lnblock)/2,20,1)
	set_img(blocks[i],"block3.png")	
	createrect(blocks[i])	
while life>0:
	for event in pygame.event.get():
                key=pygame.key.get_pressed()
		
        	if event.type == pygame.QUIT or key[pygame.K_ESCAPE]: #Se premi la croce chiude 
                        print "Vite="+str(life)+" Rimbalzi="+str(rebound)
                        pygame.quit()
                        sys.exit()
                loc=pygame.mouse.get_pos()
                baserect.left=loc[0]-40
   	ballrect = ballrect.move(speed)
    	if ballrect.left < 0 or ballrect.right > width:
        	speed[0] = -speed[0]
   	if ballrect.top < 0 or ballrect.bottom > height:
                if ballrect.bottom>=height:
                        life-=1
                        print "Morto"                                                
        	speed[1] = -speed[1]
        if baserect.left < 0 :
                baserect.left=0
        if baserect.right > width:
                baserect.right=width
        if ((ballrect.right>=baserect.left and ballrect.right<=baserect.right)or(ballrect.left>=baserect.left and ballrect.left<=baserect.right)) and  baserect.top<=ballrect.bottom:
                speed[1] = -speed[1]
                rebound+=1
        for i in range(0,len(blocks)):		
		if(blocks[i].rect.colliderect(ballrect)and blocks[i].life>0):
			if(blocks[i].rect.left<ballrect.right or blocks[i].rect.right>ballrect.left):
				speed[0]=-speed[0]				
			if(blocks[i].rect.top<ballrect.bottom or blocks[i].rect.bottom>ballrect.top):
				speed[1]=-speed[1]
			
			blocks[i].life-=1
			point+=float(life)*float(1.0/float(1+rebound-lrebound))
			lrebound=rebound
        screen.blit(back,backrect)
	screen.blit(ball, ballrect)
	screen.blit(base, baserect)
	for i in range(0,len(blocks)):
		if blocks[i].life>0:
			screen.blit(blocks[i].imgsr,blocks[i].rect)		
	testo="Vite: "
	testo=testo+str(life)
	testo=testo+" Rimbalzi: "
	testo=testo+str(rebound)
	testo=testo+" Score: "
	testo=testo+str(point)
	fps=1/(time.time()-lastf)
	lastf=time.time()
	testo+=" FPS: "+str(int(fps))
	ren=fontolo.render(testo, 1, (25,255,25))
	screen.blit(ren, (15, 10))
	pygame.display.flip()
	time.sleep(0.001)
if life==0 :
        print "Vite="+str(life)+" Rimbalzi="+str(rebound)
