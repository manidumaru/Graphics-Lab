def LCS(x, y, m, n): 
    if (m == len(x) or n == len(y)): 
        result = 0 
    elif (box[m][n] != -1): 
        result = box[m][n] 
    elif (x[m] == y[n]): 
        result = 1 + LCS(x, y, m+1, n+1) 
    else: 
        result = max(LCS(x, y, m+1, n), LCS(x, y, m, n+1)) 
    box[m][n] = result 
    
    return result 
 
 
y = "ried" 
x = "primer" 
box = [[-1 for i in range(len(y)+1)] for i in range(len(x)+1)] 
 
 
print(LCS(x, y, 0, 0)) 
# print(box)