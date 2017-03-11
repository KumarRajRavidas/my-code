'''from _ast import Num
def recurPower (base, exp):
    if exp <=0:
        return 1
    else:
        return base*recurPower(base, exp-1)
recurPower(2,3)    
print recurPower(2,3)   




def  printtringularnumber(x):
    i=1
    while i<= x:
        print i,"*",'\t'
        i +=1
printtringularnumber(8)  


          
def numdigit(n):
        count = 0
        if n==0:
            return 1
        elif n < 0:
            n = -n
            while n!=0:
                count = count + 1
                n = n / 10
                print count,
            return count
        else:
            while n!=0:
                count = count + 1
                n = n / 10
                print count,        
            return count
print numdigit(-874555) 



def evenno(n):
    count = 0
    while n!=0:
        digit = n%2
        if digit ==0:
            count= count+1
        n=n/10
    return count
print evenno(789466646)    



def reverse(n):
    if n<0:
        n=-n
        i=1
        
        while n!=0:
            
            p=n%10
            n=n/10
            i=i*10
             
        return   
            
    """no=''
    while n !=0:
        no = no +str(n%10)
        n=n/10
    return no"""
print reverse(-456313)  





def addvector(u, v):
    newlist =[]
    for index1, value1 in enumerate(u):
        for index2, value2 in enumerate(v):
            if index1 ==index2:
                newlist = newlist + [value1 + value2]
    return newlist
print addvector([4,5,2], [7,6,4])


def addvector2(u, z):
    newlist = []
    for index, value in enumerate(u):
        newlist = newlist + [u[index] + z[index]]
    return newlist 
print addvector2([4,5,2], [7,6,4])'''



def noofvol(s):
    num =0
    for letter in s:
        if letter in "aeiou":
            num=num+1
    return num   
print " no vowel of vowel is:", noofvol("dhfsdfhlsdjfhaeouiiaee") 


    
    
def noofboob(s):
    num = 0
    for i in range(1, len(s) - 1):
        if s[i-1:i+2] =='bo':
            num = num + 1
    return num
print noofboob("bobobobobobobobbbbbbbbo")

                
                
             
        

     





