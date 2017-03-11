import  exceptions
'''try:
    fil = open("/home/rinku/Desktop/New.txt","r")
    line = fil.readline()
    print line
except:
    raise Exception("cant open the file")'''
class Dog:
    __secrate=2    
    
    
def main():
    try:
        ZeroDivision=1/0
    except (ZeroDivisionError), e:
        print "you cant divided by zero"
        print e
    else:
        print ZeroDivision
    finally:
        print 'Everything is ok'
        
  
for i in dir(exceptions):
        print i
if __name__ == '__main__' : main()

###############################

'''raise exceptions
raise Exceptions
raise Exceptions('The flux capacitor is broken.')
import builtins 
dir(bulitins)
raise IOError #IOError is a class name'''
    
##############
a=input("enter value of 1st number:")  
b=input("enter value of 2nd number :") 
print 'your result is ' ,a/b #try a and b with diff values and look which type of erre apeare
##############

# Try with ecception block

try:
    a=input("enter value of 1st number:")  
    b=input("enter value of 2nd number :") 
    print 'your result is ' ,a/b
except ZeroDivisionError:
    print 'Error: DIvision by zero will not work: '
    
###############################################################    
    
'''
# Catch All Exceptions
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except:
# If any exception was raised, then execute this code block.


#Catch A Specific Exception
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except ExceptionName:
# If ExceptionName was raised, then execute this block.


#Catch Multiple Specific Exceptions
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except Exception_one:
    # If Exception_one was raised, then execute this block.
except Exception_two:
    # If Exception_two was raised, then execute this block.
else:
    # If there was no exception then execute this block.  
    
#Clean-up After Exceptions
try:
    # Your normal code goes here.
    # Your code might include function calls which might raise exceptions.
    # If an exception is raised, some of these statements might not be executed.
finally:
    # This block of code will always execute, even if there are exceptions raised

   
#An Example of File I/O
try:
    f = open("my_file.txt", "w")
    try:
        f.write("Writing some data to the file")
    finally:
        f.close()
except IOError:
    print "Error: my_file.txt does not exist or it can't be opened for output."
    
    
def main()
    A()

def A():
    B()

def B():
    C()

def C():
    try:
        D()
        except MyException:
            # execute if the MyException message happened

def D()
    # processing code
    if something_special_happened:
        aise MyException
'''

####################

#multy -exception handlar
try:
    a=float(input("enter value of 1st number:"))  
    b=float(input("enter value of 2nd number :"))
    print 'your result is ' ,a/b
except ZeroDivisionError:
    print 'Error: DIvision by zero will not work: '
except (ValueError,IOError,TypeError): #Tuple
    print 'Error: You use incorrect data type: '
    
#caching mullty -exception at once
try:
    a=float(input("enter value of 1st number:"))  
    b=float(input("enter value of 2nd number :"))
    print 'your result is ' ,a/b
except (ValueError,IOError,TypeError): #Tuple
    print 'Error: Invalid input provided: '
    
#print more dynamic exception massage text
try:
    a=input("enter value of 1st number:")
    b=input("enter value of 2nd number :")
    print 'your result is ' ,a/b
except (ZeroDivisionError,ValueError,IOError,TypeError),e: #Tuple
    print  'Error: ', e
    
#keep the program running after an exception 
while True:#remember that break/continue req. a loop
    try:
        a=input("enter value of 1st number:")  
        b=input("enter value of 2nd number :") 
        print 'your result is ' ,a/b
    except:
            print 'Invalid input please retry: '
    else:
        break

#using finally to clean up after an exception
def divlog(x,y):
    try:
        f=open('c:/files.txt' , 'a')
        f.write()
    except ZeroDivisionError:
        f.write('Error: Zero division not allowed\n')
        raise
    finally:
        f.close()
        
######################################################

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! " + str(e)
    except IOError,e:
        print 'ddddddddd'+str(e)
    except:
        print 'Invalid input please retry: '
        divide(int(x),int(y))
    else:
        print "result is", result
    finally:
        print "executing finally clause"
print divide(5,0)







