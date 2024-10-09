from enum import Enum

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
    def __init__(self,id,statuss,usname,passw,privlagee) -> None:
        self.id:int=id

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
        
    def addto(self,status,username,password,privlage):
        self.idhandle=+1
        tuser = user(self.idhandle,status,username,password,privlage)
        self.listin.append(tuser)
        
    def printall(self):
        for i in self.listin:
            print(i)

sh = spurningahandler()
uh = userhandler()

sh.addto(1,"asdasd","asdasd",1)
sh.printall()

uh.addto(1,"test",1234,1)
uh.printall()

x = privlage.Byrjandi
print(x.name)