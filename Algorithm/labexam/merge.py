
from random import sample

def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0
        while(i < len(L) and j < len(R)):
            if (L[i] < R[j]):
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1
        
        if (i > mid):
            while(j <= len(array)):
                array[k] = R[j]
                j += 1
                k += 1

        if (j > len(array)):
            while(i <= mid):
                array[k] = L[i]
                i += 1
                k += 1
    return




array = [2,0,6,1,8,9]
data = sample(range(0,10000), 100)
# print(data)
print(data)
mergeSort(data)
print(data)