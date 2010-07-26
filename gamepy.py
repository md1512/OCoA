import sys, pygame ,time
import pygame.font
import pygame.surface
pygame.init()
pygame.font.init
fontolo=pygame.font.Font(None, 25)
life=3
rebound=0
point=0
size = width, height = 1024,600
speed = [8,8]
speedb = [0,0]
screen = pygame.display.set_caption('OCoA')
screen = pygame.display.set_mode(size)
back = pygame.image.load("background.png")
ball = pygame.image.load("ball.png")
base = pygame.image.load("base.png")
baserect = base.get_rect()
ballrect = ball.get_rect()
backrect= back.get_rect()
baserect.bottom=height-10
baserect.right=(width)/2+40
while life>0:
	for event in pygame.event.get():
                key=pygame.key.get_pressed()
		
        	if event.type == pygame.QUIT or key[pygame.K_ESCAPE]: #Se premi la croce chiude 
                        print "Vite="+str(life)+" Rimbalzi="+str(rebound)
                        pygame.quit()
                        sys.exit()
                loc=pygame.mouse.get_pos()
                #print loc[0]
                #if key[pygame.K_a]:
                #        baserect.left=baserect.left-width/8      
                #if key[pygame.K_d]:
                #        baserect.right=baserect.right+width/8
                #if key[pygame.K_LEFT]:
                #        baserect.left=baserect.left-width/4
                #if key[pygame.K_RIGHT]:
                #        baserect.right=baserect.right+width/4
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
        screen.blit(back,backrect)
	screen.blit(ball, ballrect)
	screen.blit(base, baserect)
	testo="Vite: "
	testo=testo+str(life)
	testo=testo+" Rimbalzi: "
	testo=testo+str(rebound)
	testo=testo+" Score: "
	testo=testo+"Manca conteggio!"
	ren=fontolo.render(testo, 1, (25,255,25))
	screen.blit(ren, (15, 10))
	pygame.display.flip()
	time.sleep(0.00001)
if life==0 :
        print "Vite="+str(life)+" Rimbalzi="+str(rebound)+" Punti="+str(point)
