import sys, pygame ,time
pygame.init()
life=3
size = width, height = 1024,600
speed = [2,2]
speedb = [0,0]
black = 0, 0, 0
screen = pygame.display.set_caption='OCoA'
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.png")
base = pygame.image.load("base.png")
baserect = base.get_rect()
ballrect = ball.get_rect()
baserect.bottom=height
baserect.right=(width)/2+40
while life>0:
	for event in pygame.event.get():
                key=pygame.key.get_pressed()
        	if event.type == pygame.QUIT or key[pygame.K_ESCAPE]: #Se premi la croce chiude 
                        print life
                        pygame.quit()
                        sys.exit()                
                if key[pygame.K_a]:
                        speedb=[-4,0]
                if key[pygame.K_d]:
                        speedb=[+4,0]                        
   	ballrect = ballrect.move(speed)
   	baserect = baserect.move(speedb)
    	if ballrect.left < 0 or ballrect.right > width:
        	speed[0] = -speed[0]
   	if ballrect.top < 0 or ballrect.bottom > height:
                if ballrect.bottom<=height:
                        life=life-1
                        print "Merda"
        	speed[1] = -speed[1]
        if baserect.left < 0 or baserect.right > width:
                speedb=[0,0]
        if (baserect.left<=ballrect.right or baserect.right>=ballrect.right) and baserect.top<=ballrect.bottom:
                speed[1] = -speed[1]
        screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(base, baserect)
	pygame.display.flip()
	time.sleep(0.00001)
	

	


