'''num1, num2 = raw_input("enter two no ").split()
num1=int(num1)
num2=int(num2)
print 'sum is :',num1+num2

listCustNum = [0,1,2]
listCustName = ['raj das', 'amit', 'rahul']
listCustAge = [23,70,45]
for i in listCustNum:
    print '%s is %s' %(listCustName[i],listCustAge[i])
    
for i in range(1,31):
    if i%2==0:
        continue
    elif i==25:
        break
    else:
        print i,'''
a,b=10,20
c=a+b
print c

def add(*x):
    finalvalue = 0
    if x:
        for i in x:
            finalvalue +=i 
        return finalvalue
    else:
        return "please provide number"
def main():
    print add(5,6,89,78,7)     
if __name__ =='__main__': main()

