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
