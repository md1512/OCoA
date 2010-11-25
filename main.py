#!/usr/bin/env python2
import sqlite3,os
from configuration import *

try :
    os.mkdir(PATH)#Directory
except OSError:
    print "Directory exist"
#PATH=os.environ['HOME']+"/.ocoa/"

conn = sqlite3.connect(PATHDB)#Database
c = conn.cursor()
try :
    c.execute("SELECT * from USER;")
    print "maccione"
except :
    c.execute("CREATE TABLE USER(name text, id long);")
    c.execute("CREATE TABLE SCORE(score float, id long,time text);")
    print "massimiliano"
conn.commit()
c.close()

try: #Start Game
    import game
except :
    print "GAME OVER"
