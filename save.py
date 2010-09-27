import time,sqlite3,os
import configuration

def save(name,score):
    res=0    
    conn = sqlite3.connect(configuration.PATHDB)#Database    
    c = conn.cursor()
    try :
        c.execute("SELECT COUNT(id) FROM USER WHERE name=\'"+str(name)+"\';")   
        print "SELECT COUNT(id) FROM USER WHERE name=\'"+str(name)+"\';"
    except:
        print "maccione save"
    SQLnum=int(c.fetchone()[0])    
    if SQLnum>0 :
        SQLid=SQLnum+1
        print SQLid
    else:
        c.execute("SELECT MAX(id) FROM USER;")
        print "SELECT MAX(id) FROM USER;"
        a=c.fetchone()[0]        
        try:
            SQLid=long(a)+1
        except:
            SQLid=1
    c.execute("INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");")
    print "INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");"
    c.execute("INSERT INTO SCORE VALUES("+str(score)+","+str(SQLid)+",\'"+str(time.ctime())+"\');")	
    print "INSERT INTO SCORE VALUES("+str(score)+","+str(SQLid)+","+str(time.ctime())+");"
    c.close()
    conn.commit()
    conn.close()    
def hiscore():
    t=[]
    conn = sqlite3.connect(configuration.PATHDB)#Database    
    c = conn.cursor()
    try:
        c.execute("SELECT score,id  FROM SCORE ORDER BY score DESC LIMIT 0,5;")
        a= c.fetchall()
        print len(a),a
        for i in a:
            print "SELECT name FROM USER WHERE id="+str(i[1])
            c.execute("SELECT name FROM USER WHERE id="+str(i[1]))
            b=c.fetchone()
            print i[0],b[0]
            t.append(str(b[0])+ ":"+str(i[0]))
        print t        
    except:
        print "Error in save.hiscore()"
    return t
