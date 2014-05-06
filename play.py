#coding=utf-8
import os
import thread

def exeRet(cmd):
    retf = os.popen(cmd)
    rets = retf.read()
    retf.close()
    return rets

def uprint(msg):
    print msg.decode('utf8')
    
def pause(msg):
    os.system("echo "+msg+"& pause >nul")
    
class diodict(dict):
    def getkey(self,val):
        return self.keys()[self.values().index(val)]

black = [
    ("D4",),
    ("Drop",),
    ("Ever",),
    ("HD",),
    ("Ic",),
    ("Im",),
    ("ju",),
    ("KKV",),
    ("mys",),
    ("nv",),
    ("office",),
    ("ONE",),
    ("SGT",),
    ("SGI",),
    ("sql",),
    ("xmp",),
    ("taskeng",),
    ("Bai",),
    ("Bwif",),
    ("CAJ",),
    ("Flash",),
    ("Google",),
    ("Sogou",),
    ("AAM",),
    ("Update",),
    ("Qi",),
    ("QY",),
]

chcpCode = diodict({
    "英文":437,
    "日文":932,
    "简体中文":936,
    "韩文":949,
    "繁体中文":950,
    "utf-8":65001,
})

cpc = exeRet('chcp')
cpc = int(cpc[cpc.index(':')+2:len(cpc)-1])

uprint("当前编码: "+chcpCode.getkey(cpc))
objCode = 65001
uprint("目标编码: "+chcpCode.getkey(objCode))
pause("continue...")
if cpc != objCode:
    exeRet('chcp '+str(objCode))

#print u"语言: "+chcpCode.getkey(cpc).decode('utf8')

thread.start_new_thread(os.system,("echo off & systeminfo > systeminfo.txt 2>nul",))

for i in black:
    loop = 1
    if i.__len__() > 1:
        loop = i[1]
    for k in xrange(loop):
        os.system("taskkill -f -im "+i[0]+"*")
        