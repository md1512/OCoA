#!/usr/bin/python
import sqlite3,os
try :
    os.mkdir(os.environ['HOME']+"/.ocoa")#Directory
except OSError:
    print "Directory exist"
PATH=os.environ['HOME']+"/.ocoa/"

conn = sqlite3.connect(PATH+"saved")#Database
c = conn.cursor()
try :
    c.execute("SELECT * from USER")
    print "maccione"
except :
    c.execute("CREATE TABLE USER(name text, id long)")
    c.execute("CREATE TABLE SCORE(score float, id long,time text,date,text)")
    print "massimiliano"

import game #Start Game
