
def selection(data):
    for i in range(0, len(data)-1):
        smallest = i+1
        for j in range(i,len(data)-1):
            if(data[j] < data[smallest]):
                smallest = j
        # print(smallest)
        print(data[smallest])
        data[i],data[smallest] = data[smallest],data[i]

    return data



def insertion(data):
    for i in range(0,len(data)-1):
        j = i
        while (j>0 and data[j]<data[j-1]):
            data[j],data[j-1] = data[j-1],data[j]
            j = j-1
    return data

data = [2,6,1,0,3,8,4,9]
print(insertion(data))