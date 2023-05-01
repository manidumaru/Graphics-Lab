
def insertion(arr):
    for i in range(1,len(arr)):
        j = i
        while (j>0 and arr[j]<arr[j-1]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j = j-1
    return arr


def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2
		l = arr[:mid]
		r = arr[mid:]
		mergeSort(l)
		mergeSort(r)
		
		i = j = k = 0

		while i < len(l) and j < len(r):
			if l[i] <= r[j]:
				arr[k] = l[i]
				i += 1
			else:
				arr[k] = r[j]
				j += 1
			k += 1

		while i < len(l):
			arr[k] = l[i]
			i += 1
			k += 1

		while j < len(r):
			arr[k] = r[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()




# arr = [12, 11, 13, 5, 6, 7]
# print(insertion(arr))

# print("Given array is:")
# printList(arr)
# mergeSort(arr)
# print("Sorted array is:")
# printList(arr)

