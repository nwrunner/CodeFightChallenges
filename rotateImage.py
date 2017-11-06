import math
'''
Trick here is realizing that rotating 90 left or right is a transpose and a reverse of columns or rows
rotating 180 is reversing the rows and then columns (order doesn't matter)
'''
def printMatrix(matrix, size):
    formatStr = "{:>" + str(size) + "}" # pad to "size" characters
    for row in matrix:
        rowStr = ""
        for i in row:
            rowStr += formatStr.format(i)
        print( rowStr)
    
def transpose(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if (i>j):
                a[i][j], a[j][i] =  a[j][i], a[i][j]

def reverseRow(row):
    n = len(row)-1
    for x in range(math.floor((n+1)/2)):
        row[x], row[n-x] = row[n-x], row[x]
        # tmp = row[x]
        # row[x] = row[n-x]
        # row[n-x] = tmp



def rotateImage(a):
    n = len(a)
    # rotate 90 clockwise 
    transpose(a)
    for i in range(n):
        reverseRow(a[i])
'''
a = [[40,12,15,37,33,11,45,13,25,3], 
 [37,35,15,43,23,12,22,29,46,43], 
 [44,19,15,12,30,2,45,7,47,6], 
 [48,4,40,10,16,22,18,36,27,48], 
 [45,17,36,28,47,46,8,4,17,3], 
 [14,9,33,1,6,31,7,38,25,17], 
 [31,9,17,11,29,42,38,10,48,6], 
 [12,13,42,3,47,24,28,22,3,47], 
 [38,23,26,3,23,27,14,40,15,22], 
 [8,46,20,21,35,4,36,18,32,3]]
'''
a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
rotateImage(a)        
printMatrix(a,2)


print (str(hex(202))[2:])