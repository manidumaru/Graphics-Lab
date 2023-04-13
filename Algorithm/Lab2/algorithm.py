import math

def selection(arr):
    for i in range(0, len(arr)-1):
        smallest = i+1
        for j in range(i,len(arr)-1):
            if(arr[j] < arr[smallest]):
                smallest = j
        # print(smallest)
        print(arr[smallest])
        arr[i],arr[smallest] = arr[smallest],arr[i]

    return arr

def insertion(arr):
    for i in range(0,len(arr)-1):
        j = i
        while (j>0 and arr[j]<arr[j-1]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j = j-1
    return arr

def mergeSort(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        
        i=j=k=0

        while(i<len(L) and j<len(R)):
            if(arr[i] < arr[j]):
                arr[k] = arr[i]
                i+=1
            else:
                arr[k] = arr[j]
                j+=1
            k+=1
        
        while(i<len(L)):
            arr[k] = L[i]
            i+=1
            k+=1
        while(j<len(R)):
            arr[k] = L[j]
            j+=1
            k+=1




arr = [2,6,1,0,3,8,4,9]
mergeSort(arr)
print(arr)

