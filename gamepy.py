#!/usr/bin/python
import sys,time,random
from libblock import *
import pygame,pygame.font,pygame.surface

def stmp(tmp):
	itmp = pygame.image.load(get_img(tmp))
	itmrect=itmp.get_rect()
	itmrect.top=tmp.y
	itmrect.left=tmp.x
	screen.blit(itmp,itmrect)

pygame.init()
pygame.font.init
fontolo=pygame.font.Font(None, 25)
life=3
rebound=0
point=0
size = width, height = 1024,600
lnblock=100
speed = [8,8]
screen = pygame.display.set_caption('OCoA')
screen = pygame.display.set_mode(size)
back = pygame.image.load("background.png")
ball = pygame.image.load("ball.png")
base = pygame.image.load("base.png")
baserect = base.get_rect()
ballrect = ball.get_rect()
backrect= back.get_rect()
baserect.bottom=height-10
baserect.right=(width)/20+40
blocks=[]

for i in range(0,width/lnblock):
	blocks.append(block())
	set_pos(blocks[i],i*(width/10)+(width/10-lnblock)/2,20,1)
	set_img(blocks[i],"block2.png")
	print get_pos(blocks[i])
	stmp(blocks[i])
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
                #point+=point+rebound**life
	ltouched=0
	utouched=0
	for i in range(0,len(blocks)):
		if (blocks[i].x ==ballrect.right or blocks[i].x+lnblock ==ballrect.left) and blocks[i].life>0 and ballrect.bottom<blocks[i].y+40 and ballrect.top> blocks[i].y :
			ltouched=i+1
		if (blocks[i].y+40 ==ballrect.top or blocks[i].y ==ballrect.bottom )and blocks[i].life>0 and ballrect.left<blocks[i].x+lnblock and ballrect.right>blocks[i].x:
			utouched=i+1
	if utouched != 0 :
		
		speed[1]=-speed[1]
		blocks[utouched-1].life-=1
		utouched=0
		print "massimiliano"
	if ltouched != 0 :
		print "maccione"
		speed[0]=-speed[0]
		blocks[ltouched-1].life-=1
		ltouched=0	
        screen.blit(back,backrect)
	screen.blit(ball, ballrect)
	screen.blit(base, baserect)
	for i in range(0,len(blocks)):
		if blocks[i].life>0:
			stmp(blocks[i])		
	testo="Vite: "
	testo=testo+str(life)
	testo=testo+" Rimbalzi: "
	testo=testo+str(rebound)
	testo=testo+" Score: "#A si'? rimbalzi(ita) punteggio(ita) e Score(eng)? 
	testo=testo+"Manca conteggio!"
	ren=fontolo.render(testo, 1, (25,255,25))
	screen.blit(ren, (15, 10))
	pygame.display.flip()
	time.sleep(0.00001)
if life==0 :
        print "Vite="+str(life)+" Rimbalzi="+str(rebound)



