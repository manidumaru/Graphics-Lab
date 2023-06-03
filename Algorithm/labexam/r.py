# from random import sample

def counting(arr, c):
    b = [0 for i in range(0,len(arr))]
    for i in arr:
        c[i] += 1
    print(arr)
    
    for i in range(0, 9):
        if i == 0:
            pass
        else:
            c[i] = c[i] + c[i-1]
    print(c)
    for i in range(len(arr)-1, -1, -1):
        b[c[arr[i]]-1] = arr[i]
        c[arr[i]] -= 1
    return b


array = [0,5,6,6,8,1,0,0,2,1,1,3]
c = [0 for i in range(0, max(array)+1)]
print(counting(array, c))
