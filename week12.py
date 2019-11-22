#Aiden Reeves
#CSCI 102- Section B
#Week 12A
def PrintOutput(a):
    print("OUTPUT",a) #This is the first function that just makes it print output
def LoadFile(b):
    b=input("Enter file name: ")
    with open(b,'r')as ins:
        array=[] #this is to read a file line by line
        for line in ins:
            array.append(line)
    PrintOutput(array)
def UpdateString(a,b,c):
    alist=list(a.split(""))
    alist[c]=b
    PrintOutput(alist)
def FindWordCount(a,b):
    x=0
    st=[ch for ch in b]
    while x<len(a):
        if a[x]==st[x]:
            z=1
            c=1
            q=0
            while q<len(b)-1:
                if x+z>= len(a):
                    my_confidence=0
                elif a[x+z]:
                    c+=1
                z+=1
                q+=1
            if c== len(b):
                n+=1
        x+=1
    PrintOutput(n)
def ScoreFinder(a,b,c): 
    yourmom=0
    yourdad=0
    t=0
    if t<len(a):
        if a[t]==c:
            yourdad=b[t]
            yourmom=1
        t+=1
    if yourmom==1:
        hello=(c,", got a score of",yourdad)
        PrintOutput(hello)
    else:
        hello="player not found"
        PrintOutput(hello)
def Union(a,b):
    u=0
    r=0
    while u<len(a):
        while r<len(a):
            if a(u)==b(r):
                del b[r]
            r+=1
        u+=1
    jello=a+b
    PrintOutput(jello)
def Intersection(a,b):
    u=0
    r=0
    wheat=[]
    while u<len(a):
        while r<len(a):
            if a(u)==b(r):
                wheat.append(a[u])
            r+=1
        u+=1
    PrintOutput(wheat)
def Notln(a,b):
    u=0
    r=0
    while u<len(a):
        while r<len(a):
            if a(u)==b(r):
                del a[u]
            r+=1 #ask if this will work
        u+=1
    PrintOutput(a)
