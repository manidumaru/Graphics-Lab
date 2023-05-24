from prettytable import PrettyTable

def LCS(w1, w2, m , n):
    if (mat[m][n] != 0):
        result = mat[m][n]
    if (m == len(w1) or n == len(w2)):
        result = 0
    elif(w1[m] == w2[n]):
        result = 1 + LCS(w1,w2,m+1,n+1)
    else:
        result = max(LCS(w1,w2,m+1,n), LCS(w1,w2,m,n+1))
    mat[m][n] = result
    return result


w1 = "AC"
w2 = "TAGC"

mat = [[0 for _ in range(len(w2) + 1)] for _ in range(len(w1) + 1)]
length = LCS(w1,w2,0,0)
print(length)

########################################################################################
arr = []
x = PrettyTable()

for i in range(len(w2)):
    arr.append(w2[i] + str(i))
arr.append("/0")
x.field_names = arr
arr = []

for i in range((len(w1)+1)):
    for j in range((len(w2)+1)):
        arr.append(mat[i][j])
    x.add_row(arr)
    arr = []

print(x)


