#get middle digts. NOTE: round down for odd values of k
def getMiddleKth(strInput,k):
    startIndex = (len(strInput) - k)/2 
    return strInput[startIndex: startIndex+k]

def random1(seed, n):
    seedLen = len(str(seed))
    while (n != 0):
        strSeed = str(seed * seed)
        if (seedLen*2 > len(strSeed)):
            pad = "0" * (seedLen*2 - len(strSeed)) 
            strSeed = pad + strSeed
        newSeed = int(getMiddleKth(strSeed, seedLen))
        print "seed=" + str(seed) + " squared=" + strSeed + " nextSeed=" + str(newSeed) 
        seed = newSeed
        n -= 1
        
    return seed

print random1(881231, 23)
