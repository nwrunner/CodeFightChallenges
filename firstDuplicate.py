def firstDuplicateWithSpace(a):
    myList = [0] * len(a)
    for val in a:
        if (myList[val-1] != 0):
            return val
        myList[val-1] = val
    return -1


def firstDuplicate(a):
    # this doesn't guarantee the first duplicate
    spareNum = -1
    for i, val in enumerate(a):
        valIdx = val-1
        if (a[valIdx] == val and i != valIdx):
            return val
        
        while (i != valIdx):
            i = valIdx
            newVal = a[valIdx]
            a[valIdx] = val
            valIdx = newVal-1
            val = newVal
    return -1



test = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
print(test)
print(firstDuplicateWithSpace(test), firstDuplicate(test))

test = [2, 3, 3, 1, 5, 2]
print(test)
print(firstDuplicateWithSpace(test), firstDuplicate(test))
print(test)

