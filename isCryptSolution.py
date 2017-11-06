import math

def w2n(word, letterDict):
    # convert word to number

    retVal = 0
    
    for tens, i in enumerate(word[::-1]):
        retVal += math.pow(10,tens) * letterDict[i]


    if tens > 0 and retVal < math.pow(10,tens):
        return -1
    return retVal

def isCryptSolution(crypt, solution):
    letterDict = {}
    for i in solution:
        letterDict[i[0]] = int(i[1])
        
    w1 = w2n(crypt[0], letterDict)
    w2 = w2n(crypt[1], letterDict)
    w3 = w2n(crypt[2], letterDict)
    
    if (w1 == -1 or w2 == -1 or w3==-1):
        return False
    
    return (w1 + w2 == w3)

crypt= ["AA", 
 "AA", 
 "AA"]
solution= [["A","0"]]

isCryptSolution(crypt, solution)