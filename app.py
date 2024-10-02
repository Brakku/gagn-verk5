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
    def __init__(self,num,intype,title,text) -> None:
        self.id:int =num
        self.type:stype =stype.new(intype)
        self.title:str =title
        self.text:str =text
        
    def __str__(self) -> str:
        return f"id: {self.id}, type: {self.type.name}, title {self.title}, text: {self.text}"
    
class spurningahandler:
    
    def __init__(self):
        self.listin = []
        
    def addto(self,type,title,text):
        
        tspur = spurning(len(self.listin)+1,type,title,text)
        self.listin.append(tspur)
        
    def printall(self):
        for i in self.listin:
            print(i)
    
class status(Enum):
    Virkur =0
    Óvirkur =1
    Tímabundiðbann =2
    Bann =3
    
class privlage(Enum):
    Byrjandi =0
    Hefðbundinn =1
    Lengrakominn =2
    Súpernotandi =3
    Stjórnandi =4
    
class user:
    def __init__(self,id,status,privlage) -> None:
        self.id:int=id
        self.status:status=status
        self.privlage:privlage=privlage


sh = spurningahandler()

sh.addto(1,"asdasd","asdasd")
sh.printall()