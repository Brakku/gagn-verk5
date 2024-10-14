from enum import Enum
from hashlib import sha256
import psycopg2

def connecter():
    conn = psycopg2.connect("dbname=lokaverk user=postgres password=1234")
    conn.autocommit = True
    cur = conn.cursor()
    print("connected")
    return cur


class stype(Enum):
    Forritun = 0
    Gagnagrunnar = 1
    Leikjaforitun = 2
    KerfisstjórnunLinux =3
    KerfisstjórnunWindows =4
    Róbótar=5
    Vefþróun=6
    Annað=7
    
    def new(num):
        match num:
            case 0:
                return stype.Forritun
            case 1:
                return stype.Gagnagrunnar
            case 2:
                return stype.Leikjaforitun
            case 3:
                return stype.KerfisstjórnunLinux
            case 4:
                return stype.KerfisstjórnunWindows
            case 5:
                return stype.Róbótar
            case 6:
                return stype.Vefþróun
            case 7:
                return stype.Annað
    
class spurning:
    def __init__(self,num,intype,title,text,author) -> None:
        self.id:int =num
        self.author=author
        self.type:stype =stype.new(intype)
        self.title:str =title
        self.text:str =text
        
    def __str__(self) -> str:
        return f"id: {self.id}, type: {self.type.name}, title {self.title}, text: {self.text}"
    
class spurningahandler:
    
    def __init__(self):
        self.listin = []
        self.idhandle=0
        
    def addto(self,type,title,text,auth):
        self.idhandle=+1
        tspur = spurning(self.idhandle,type,title,text,auth)
        self.listin.append(tspur)
        
    def printall(self):
        for i in self.listin:
            print(i)
    
class status(Enum):
    Virkur =0
    Óvirkur =1
    Tímabundiðbann =2
    Bann =3
    annad=4
    
    def new(num):
        match num:
            case 0:
                return status.Virkur
            case 1:
                return status.Óvirkur
            case 2:
                return status.Tímabundiðbann
            case 3:
                return status.Bann
            case 4:
                return status.annad
    
class privlage(Enum):
    Byrjandi =0
    Hefðbundinn =1
    Lengrakominn =2
    Súpernotandi =3
    Stjórnandi =4
    annad=5
    
    def new(num):
        match num:
            case 0:
                return privlage.Byrjandi
            case 1:
                return privlage.Hefðbundinn
            case 2:
                return privlage.Lengrakominn
            case 3:
                return privlage.Súpernotandi
            case 4:
                return privlage.Stjórnandi
            case 5:
                return privlage.annad
    
class user:
    def __init__(self,id,statuss,usname,passw,privlagee,rating) -> None:
        self.id:int=id
        self.rating=rating
        self.status=status.new(statuss)
        self.username=usname
        self.password=passw
        self.privlage=privlage.new(privlagee)
        self.spurningar=[]
    
    def __str__(self) -> str:
        return f"id: {self.id}, status: {self.status.name}, username: {self.username}, password: {self.password}, privlage: {self.privlage.name} numer af spurningum: {len(self.spurningar)}"

class userhandler:
    
    def __init__(self):
        self.listin = []
        self.idhandle=0
        
    def addto(self,status,username,password,privlage,rating):
        self.idhandle=+1
        tuser = user(self.idhandle,status,username,password,privlage,rating)
        self.listin.append(tuser)
        
    def printall(self):
        for i in self.listin:
            print(i)
            


class Datamanager:
    cur = connecter()
    
    def __init__(self):
        self.iduser=0
        self.idspur=0
        self.idlausn=0
        
        self.idgetter()
    
    def idgetter(self):
        query =f"select count(uid) from users"
        self.cur.execute(query)
        uid = self.cur.fetchall()
        self.iduser = uid[0][0]
        
        query =f"select count(sid) from spurningar"
        self.cur.execute(query)
        sid = self.cur.fetchall()
        self.idspur = sid[0][0]
        
        query =f"select count(lid) from lausnir"
        self.cur.execute(query)
        lid = self.cur.fetchall()
        self.idlausn = lid[0][0]
    

    def adduser(self,username,password,status,privlage):
        self.iduser +=1
        
        encripted = sha256(password.encode('utf-8')).hexdigest()
        
        x= f"{self.iduser},'{username}','{encripted}',{status},{privlage}"
        
        query =f"call adduser({x})"
        
        try:
            self.cur.execute(query)
        except psycopg2.errors.UniqueViolation:
            print("nafn er tekið")
        except:
            print("villa")
        
    def upuser(self,id,username,password,status,privlage):
        
        encripted = sha256(password.encode('utf-8')).hexdigest()
        x= f"{id},'{username}','{encripted}',{status},{privlage}"
        
        query =f"call upuser({x})"
        try:
            self.cur.execute(query)
        except psycopg2.errors.UniqueViolation:
            print("nafn er tekið")
        except:
            print("villa")
        
    def deluser(self,id):
        x= f"{id}"
        
        query =f"call deluser({x})"
        self.cur.execute(query)
    
    def loadusers(self):
        
        query =f"select * from users"
        self.cur.execute(query)
        uslist = self.cur.fetchall()
        for user in uslist:
            print(user)
            
    
            
    def addspurning(self,author,stype,title,text):
        self.idspur+=1
        x= f"{self.idspur},{author},{stype},'{title}','{text}'"
        
        query =f"call addspurning({x})"
        self.cur.execute(query)
        
    def upspurning(self,id,author,stype,title,text):
        x= f"{id},{author},{stype},'{title}','{text}'"
        
        query =f"call upspurning({x})"
        self.cur.execute(query)
        
    def delspurning(self,id):
        x= f"{id}"
        
        query =f"call delspurning({x})"
        self.cur.execute(query)
    
    def loadspurning(self):
        
        query =f"select * from spurningar"
        self.cur.execute(query)
        splist = self.cur.fetchall()
        for spurningar in splist:
            print(spurningar)
            
            
    
    def addlausn(self,author,spurning,texti,rating):
        if rating >0 or rating <10:
            self.idlausn +=1
            
            x= f"{self.idlausn},{author},{spurning},'{texti}',{rating}"
            
            query =f"call addlausn({x})"
            
            try:
                self.cur.execute(query)
            except:
                print("villa")
        else:
            print("rating of hátt/lágt")
            
    def loadlausnir(self):
        
        query =f"select * from lausnir"
        self.cur.execute(query)
        laulist = self.cur.fetchall()
        for lausnir in laulist:
            print(lausnir)
            
    def spurcount(self,uid): # liður 4 1
    
        query =f"SELECT count(sid) from spurningar WHERE author_id = {uid}"
        self.cur.execute(query)
        laulist = self.cur.fetchall()
        for lausnir in laulist:
            print(lausnir[0])
            
    def idadmin(self,uid): # liður 4 2
        
        query =f"SELECT privlage from users WHERE uid = {uid}"
        self.cur.execute(query)
        laulist = self.cur.fetchall()
        if laulist[0][0]==4:
            return True
        else:
            return False
        
    def ratinggetter(self,uid): # liður 4 1
        
        query =f"SELECT rating from lausnir WHERE lid = {uid}"
        self.cur.execute(query)
        laulist = self.cur.fetchall()
        return laulist[0][0]
            
    
    def admingetprivlage(self,privlage,adminid,admpass):
        
        query =f"select passw from users where privlage = 4 and uid = {adminid}"
        self.cur.execute(query)
        adminpassreal = self.cur.fetchall()
        if adminpassreal[0][0] == sha256(admpass.encode('utf-8')).hexdigest():
            
            query =f"select * from users where privlage = {privlage}"
            self.cur.execute(query)
            list = self.cur.fetchall()
            for lausnir in list:
                print(lausnir)
            
    def adminchangestatus(self,uid,nstatus,adminid,admpass):
        
        try:
            query =f"select passw from users where privlage = 4 and uid = {adminid}"
            self.cur.execute(query)
            adminpassreal = self.cur.fetchall()
            if adminpassreal[0][0] == sha256(admpass.encode('utf-8')).hexdigest():
                
                x= f"{uid},{nstatus}"
                
                query =f"call adminchangestatus({x})"
                self.cur.execute(query)
            
            else:
                print("incorrect credentials")
        except:
            print("villa")    
    
    def __str__(self) :
        return f"connection: {self.cur}"


dm = Datamanager()

dm.adduser("testuser1","1234",0,1)
dm.adduser("testuser2","1234",0,1)
dm.adduser("testuser3","1234",0,1)

dm.adduser("admin","1",0,4)
print()

dm.addlausn(2,1,"awa",1)

print(dm.ratinggetter(1))



dm.loadusers()

print(dm.idadmin(2))
print(dm.idadmin(1))

#dm.spurcount(1)

#dm.loadusers()
print()

#dm.adminchangestatus(1,0,2,"1")

#dm.admingetprivlage(0,2,"1234")

print()


"""
dm.adduser("abba","1234",1,1,1)
dm.adduser("abba","1234",1,1,1)
dm.loadusers()
dm.upuser(1,"virkar","1234",2,2,2)
print()
dm.loadusers()
dm.deluser(1)
print()
dm.loadusers()
"""

"""
dm.addspurning(1,1,"a","aa")
dm.loadspurning()
"""

"""
sh = spurningahandler()
uh = userhandler()

sh.addto(1,"asdasd","asdasd",1)
sh.printall()

uh.addto(1,"test",1234,1,1)
uh.printall()

x = privlage.Byrjandi
print(x.name)
"""