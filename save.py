import time,sqlite3,os
PATH=os.environ['HOME']+"/.ocoa/"
def save(name,score):
    res=0
    #try:
    conn = sqlite3.connect(PATH+"saved")#Database
    print PATH+"saved"
    c = conn.cursor()
    try :
        c.execute("SELECT COUNT(id) FROM USER WHERE name=\'"+str(name)+"\';")   
        print "SELECT COUNT(id) FROM USER WHERE name=\'"+str(name)+"\';"
    except:
        print "maccione save"
    SQLnum=int(c.fetchall()[0][0])
    print SQLnum
    if SQLnum>0 :
        SQLid=long(c.fetchone()[0])		
        print SQLid
    else:
        c.execute("SELECT MAX(id) FROM USER;")
        print "SELECT MAX(id) FROM USER;"
        SQLid=long(c.fetchone()[0])+1
        print SQLid
    c.execute("INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");")
    print "INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");"
    c.execute("INSERT INTO SCORE VALUES("+str(score)+","+str(SQLid)+",\'"+str(time.ctime())+"\');")	
    print "INSERT INTO SCORE VALUES("+str(score)+","+str(SQLid)+","+str(time.ctime())+");"
    c.close()
    conn.commit()
    conn.close()
    #except:
    #    print "massimiliano save"
