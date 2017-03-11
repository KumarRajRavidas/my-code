'''def selection(A):
    for i in range(len(A)-1):
        iMin = i
        for j in range(i+1,len(A)):
            if A[j] < A[iMin]:
                iMin = j 
        temp = A[i]
        A[i] = A[iMin]
        A[iMin] = temp
A = ['a','z','e','i','b',56.-8,.34,5,9,6]
selection(A)  
print A'''

'''def insertion(A):
    for i in range(1,len(A)):
        value = A[i]
        hole = i 
        while hole > 0 and A[hole-1] > value:
            A[hole] = A[hole-1]
            hole = hole - 1
        A[hole] = value
A = ['a','z','e','i','b',56.-8,.34,5,9,6]   
insertion(A)
print A     

def bubble(A):
        for i in range(len(A) - 2):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
A = ['a','z','e','i','b',56.-8,.34,5,9,6]   
bubble(A)
print A'''     

#####################  Merge sort ###############################

'''def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        right = mergeSort(L[middle:])
        left = mergeSort(L[:middle])
        return merge(left, right)
    

def merge(left, right):
    result =[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
L=[2,5,7,5,0,3,6,3,45,23,7,90,0,-6,-90,67]
print (mergeSort(L))'''


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)




    
        
    




    
    
        
        
##################### Quick Sort ######################
  


'''def partition(L, start, end):
    pivot =L[-1]
    pi = start 
    for i in range(start, len(L)- 1):
        if L[i] <= pivot:
            temp = L[i]
            L[i] = L[pi]
            L[pi] = temp
            pi = pi+1
    
    temp = L[pi]
    L[pi] = L[len(L) -1]
    L[len(L) -1] = temp
    return pi

def Qucksort(L, start, end):
    if start <  end:
        pi = partition(L, start, end)
        Qucksort(L, start, pi-1)
        Qucksort(L, pi+1, end)
        
    
L = [5,5,6,7,1,3,4,1,5,3]  
Qucksort(L, 0, len(L)-1)
print L'''


















