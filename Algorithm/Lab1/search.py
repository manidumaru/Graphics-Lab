from math import floor

def linear_search(data, target):
    for i in range(len(data)):
        if (data[i] == target):
            return i
    return -1

def binary_search(data, target, l_index, r_index):
    mid = (l_index + r_index)/2
    mid = floor(mid)

    try:
        if (target > data[mid]):
            l_index = mid + 1
            return binary_search(data, target, l_index, r_index)
        elif (target < data[mid]):
            r_index = mid - 1
            return binary_search(data, target, l_index, r_index)
        else:
            return mid
    except:
        return -1


