import time,sqlite3,os
import configuration

def save(name,score):
    res=0
    conn = sqlite3.connect(configuration.PATHDB)#Database    
    c = conn.cursor()
    c.execute("SELECT id FROM USER WHERE name=\'"+str(name)+"\';")
    a=c.fetchone()
    if a==None:
        c.execute("SELECT MAX(id) FROM USER;")
        print "SELECT MAX(id) FROM USER;"
        b=c.fetchone()[0]
        print b
        if b==None:
            SQLid=1
        else:
            SQLid=long(b)+1
        c.execute("INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");")
        print "INSERT INTO USER VALUES(\'"+name+"\',"+str(SQLid)+");"
    else:
        SQLid=long(a[0])
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
            c.execute("SELECT name FROM USER WHERE id="+str(i[1])+";")
            b=c.fetchone()
            print i[0],b[0]
            t.append(str(b[0])+ ":"+str(i[0]))
        print t        
    except:
        print "Error in save.hiscore()"
    return t
