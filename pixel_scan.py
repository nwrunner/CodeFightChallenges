def point_in_rects(m,n, rects):
    # returns true if the point is in any of the rectangles found so far
    for (i,j), (x,y) in rects:
        if m >= i and m <= x and n >= j and n <= y:
            return True
    return False

def scan(input):
    # assume input is a list of lists
    rects = [] # store tuples of two coordinates

    steps = 0
    i = 0
    while i < len(input):    
        j = 0
        while j < len(input[i]):
            steps += 1
            if input[i][j] == 1: # found a new start (maybe)
                if point_in_rects(i,j, rects):
                    j += 1
                    continue
                
                x = i
                while (input[x][j] == 1): 
                    x += 1
                    if x >= len(input): # boundry check
                        break
                x -= 1 # x  should the lowest part of the rect

                y = j
                while (input[i][y] == 1):
                    y += 1
                    if y >= len(input[i]):
                        break
                y -= 1  

                print(f"Found a rect ({i}, {j}) ({x}, {y})")            
                rects.append( ((i,j), (x,y)) )
                j = y
            j += 1
        i += 1

    print (f"Found {len(rects)} rectangle(s) in {steps} steps")
    


scan([[ 0, 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 1, 1, 0, 1, 1 ],
    [ 0, 0, 0, 0, 0, 1, 1 ],
    [ 0, 0, 0, 0, 0, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0 ],
    [ 1, 1, 1, 1, 0, 0, 0 ],
    [ 1, 1, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 1, 1 ] ])

