import time,sqlite3,os
PATH=os.environ['HOME']+"/.ocoa/"
def save(name,score):
    res=0    
    conn = sqlite3.connect(PATH+"saved")#Database
    print PATH+"saved"
    c = conn.cursor()
    try :
        c.execute("SELECT COUNT(id) FROM USER WHERE name=\'"+str(name)+"\';")   
        print "SELECT COUNT(id) FROM USER WHERE name=\'"+str(name)+"\';"
    except:
        print "maccione save"
    SQLnum=int(c.fetchone()[0])
    print SQLnum
    if SQLnum>0 :
        SQLid=SQLnum+1
        print SQLid
    else:
        c.execute("SELECT MAX(id) FROM USER;")
        print "SELECT MAX(id) FROM USER;"
        a=c.fetchone()[0]
        #if a[0]!="None":
        #print a
        try:
            SQLid=long(a)+1
        except:
            SQLid=1
#            print a[0]
        print SQLid
    c.execute("INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");")
    print "INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");"
    c.execute("INSERT INTO SCORE VALUES("+str(score)+","+str(SQLid)+",\'"+str(time.ctime())+"\');")	
    print "INSERT INTO SCORE VALUES("+str(score)+","+str(SQLid)+","+str(time.ctime())+");"
    c.close()
    conn.commit()
    conn.close()    
def hiscore():
    print "mac"
