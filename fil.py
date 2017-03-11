'''import os
fil = open("C:\\Users\\rinku\\Desktop\\New.txt", "r")
for aline in fil:
 
    values = aline.split()  #valus is the list string ,value=[' 0', '1' .......,'10']
    
    print values[0],'|' ,values[1],'|' ,values[10] 
    print values
    print aline

fil.close()'''


'''fil = open("C:\\Users\\rinku\\Desktop\\New.txt","r")
newlist=[]
#outfile = open("qbnames.txt", "w")

line = fil.readline() #its one line of the txt
k=0
sumofno=0
while line:
    items = line.split()
    print items
    print line
    newlist.append(items[10])
    #dataline = items[1] + ',' + items[0]
    #outfile.write(dataline + '\n')
    sumofno= sumofno + float(items[10])
    line = fil.readline()
    k=k+1
avg=sumofno/k
print avg
print "The new list is" ,newlist '''

def retriveFile():
    try: # will catch any error  if the file doesn't exist
        bestStudent = {} # dictinory  
        bestStudentStr ="The Best Student Ranked\n\n"

        f=open("C:\\Users\\rinku\\Desktop\\newt.txt")

    except(IOError), e:
        print "File is not found" ,e
    else:
        for line in f:
         
            name, grade, x = line.split()
            bestStudent[grade ] = name
            print line
            print name 
            print grade
            print x
            print bestStudent
            
        f.close()

        for i in sorted(bestStudent.keys(), reverse=True): # it give sorted no ,ie key 9 8 7 6 5 like that  so bestStudent[9(key)]=value
            print(bestStudent[i] + '  scord a  ' + i +"\n")
            print bestStudent[i]
            bestStudentStr +=bestStudent[i]  + '  scord a  ' + i +"\n"

        print '\n'

        print bestStudentStr
    # Output the string to a new fie 'w' stand for write to file
        outToFile = open("C:\\Users\\rinku\\Desktop\\newopt.txt","w")
        outToFile.write(bestStudentStr)
    #close the file which creat
        outToFile.close()
        print 'finishd update'
    return
def main():
    retriveFile()
if __name__ == '__main__' : main()    




