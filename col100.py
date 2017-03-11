'''import math
def hypo(base, height):
    squart = base**2 + height**2
    return (math.sqrt(squart))
print hypo(23,78) 
import math
def hypo(base):
    return (math.sqrt(base))
print hypo(4)       
   
base=input("enter value of base :")   
height=input("enter value of height :")  
x = base**2 + height**2
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print abs(ans**2 - x)
    print x
    print ans
    #print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    #numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
#print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x)) 


s='234jghjfgj67658808089y   cfsdfs'
for value in s:
    print value




    
n=23455868
no=0
while n!=0:
    n=n/10
    no=no+1    
total= 10**no
print total
n=234
for i in range(1,no):
    n=n/total
    print n
    n=n%total
    total=total/10
    
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:   
            print a,
            a, b = b, a+b    
    
def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result    '''




''''a=input("enter value of 1st number:")  
b=input("enter value of 2nd number :") 
def display(choice,a,b):
    if choice=='a' or 'A':
        return addnumber(a,b)
    elif choice=='D':
        return dividno(a,b)
    elif choice=='S':
        return substr(a,b)
    else:
        print "invalid choice"
    
def addnumber(a,b): 
    return a+b
def dividno(a,b): 
    return a/b
def substr(a,b):
    return a-b
choice=raw_input("enter your choice :") 
print display(choice,a,b)'''


'''def dispatch(choice):
    if choice == 'a':
        function_a()
    elif choice == 'b':
        function_b()
    elif choice == 'c':
        function_c()
    else:
        print "Invalid choice."
def function_a():
    print "function_a was called ..."
def function_b():
    print "function_b was called ..."
def function_c():
    print "function_c was called ..."
choice = raw_input ("Please Enter a Function.")
dispatch(choice)'''   


'''no=[]
a=1000
b=2000
j=13000
for i in range(a,b+1):
    if i%11==0 and (i*11)%13==0:
        no.append(i)
        print i
       
print no'''


'''for a in range(20):
    print a,
    for b in range(20):
        #print b
        for c in range(20):
           # print c
            for d in range(20):
                #print d
                if a**3 + b**3 == c**3 + d**3 and a!=b and a!=c and a!=d and b!=c and b!=d:
                    print a**3+b**3
                    print a,b,c,d'''
                    



                    
                   
                   
                
                   
    


      
    
    
    
     
    



        