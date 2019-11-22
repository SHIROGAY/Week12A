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
