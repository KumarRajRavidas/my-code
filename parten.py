for i in range(1,5):
    for j in range(1,i+1):
        print '* ',
    print ' '  
        
        
ran = input("Upto how many line ? ")
rang = int(ran)
k = 1
for i in range(1, rang+1):
    for j in range(1, i+1):
        print k,
        k = k + 1
    print '-'
    k=1



k = 5
t=1
for i in range(0,5):
    for j in range(1,k):  #for space printing
        print '_',
    k = k - 1
    for j in range(0,t):  #for star printing
        print '*',
    t=t+2
    print ''
    
    
    
for i in range(0, 5):
    for j in range(5, i, -1):
        print j,
    print ' '   
    
 
k = 9
t=1
for i in range(0,5):  #for no loop or no of line
    for j in range(1,k):  #for space printing
        print '_',
    k = k - 2
    for j in range(0,t):  #for star printing
        print '*',
    t=t+2
    print ''   
print '' 
print ''  
    
    
 
k = 9
t=1
for i in range(0,5):  #for no loop or no of line
    for j in range(1,k):  #for space printing
        print '-',
    k = k - 1
    for j in range(0,t):  #for star printing
        print '*',
    t=t+1
    print ''   
print '' 
print ''     
    
    
    
    
    
k = 20
t=2
p=1
for i in range(0,10):  #for no loop or no of line
    for j in range(1,k):  #for space printing
        print ' ',
    k = k - 1
    for j in range(1,t):  #for number printing
        print j,
    t=t+1
    for l in range(1,i+1): #for other side print in de order
        print p,
        p=p-1
    p=i+1    
    print ''   
print ''
print ''
    
    


k = 9
t=1
for i in range(0,10):  #for no loop or no of line
    for j in range(1,i+1):  #for star printing
        print '',t,
        t=t-1
    t=i+1
    print ''   
print '' 
print ''     
    
    
k =14
t=1
for i in range(1,15):  #for no loop or no of line
    for j in range(1,k):  #for space printing
        print ' ',
    k = k - 1
    for j in range(1,i+1):  #for no printing
        print t,
        t=t+1
    print '='
print '' 
print ''


    
    

   
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    