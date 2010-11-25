import os,platform
size = width, height = 1024,600
lnblock=100
speed = [3,3]
if (platform.system()=='Linux'):
    slash='/'
    PATH=os.environ['HOME']+slash+".ocoa"+slash
else:
    if (platform.system()=='Windows'):
        slash='\\\\'
        PATH=os.environ['HOMEPATH']+slash+".ocoa"+slash


#PATH=os.environ['HOME']+"/.ocoa/"
PATHDB=PATH+"saved"
IMGPATH="images"+slash
