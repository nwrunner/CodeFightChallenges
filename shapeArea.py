'''
1
5   = 1 + 3 + 1
13  = 1 + 3 + 5 + 3 + 1
25  = 1 + 3 + 5 + 7 + 5 ...
'''
def shapeArea(n):
    if n <= 1:
        return n
    
    prev = 1 # keep count of the previous odd integer
    size = 1
    for i in range(1,n):
        size += (2*prev) + 2
        prev += 2
    return size

import math
roads = [315, 266, 180]
paths = [math.fabs(x - 45) for x in roads]
paths = [x - 180 if x > 180 else x for x in paths]
print(paths) 
print(min(paths))
