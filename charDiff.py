# Gets the best match of two strings (by length)
# return the answer as an array of [idxO, idxO, len]
def getBestMatch(oldString,newString):
    if (oldString == "" or newString == ""):
        return (0,0,0)

    #print "Calling BestMatch: " + oldString + " & " + newString

    idxO = 36
    idxN = 36
    maxLen = 0
    i = 0
    while i < len(oldString):
        j = 0
        while j < len(newString):
            #print ("checking " +oldString[i] + " vs " + newString[j] )
            if (oldString[i] == newString[j]):
                #print ("match found index " + str(i) + " and " + str(j))
                currLen = 0
                currIdxO = i
                currIdxN = j
                while (currIdxO < len(oldString) and currIdxN < len(newString)) and \
                    (oldString[currIdxO] == newString[currIdxN]):
                    # loop through until I no longer find a match, check length and set
                    # increment i and j += currLen, continue outer loops
                    currLen+=1
                    currIdxO+=1
                    currIdxN+=1
                # done with while loop, check to see if the current lenth match is greater than last best match        
                if (currLen > maxLen):
                    #print (" Larger match found:len=" + str(currLen) + " at i=" + str(i) + " j=" + str(j))
                    maxLen = currLen
                    idxO = i
                    idxN = j
                elif (currLen == maxLen):
                    # match length is the same, check to see if the match is earlier
                    if (i+j) < (idxO + idxN):
                        #print " Match found earlier:(" + str(i) + "," + str(j) + ") vs (" + str(idxO) + "," + str(idxN) + ")"
                        idxO = i
                        idxN = j
                    elif (i+j) == (idxO + idxN) and i > idxO:
                        #print " match is the same, prioritize i over j:(" + str(i) + "," + str(j) + ") vs (" + str(idxO) + "," + str(idxN) + ")"
                        idxO = i
                        idxN = j

            # end if of match
            j+=1
        i+=1

    answer = (idxO, idxN, maxLen)         
    #print " BestMatch is '" + oldString + "' and '" + newString + "' is: " + str(answer)
    return answer
### end getBestMatch

def displayDiff(oldVersion,newVersion, depth):
    output = ""

    depth += 1

    bestMatch = getBestMatch(oldVersion, newVersion)
    matchLen = bestMatch[2]
    # no additional match found in strings, base case
    if (matchLen == 0):
         if (len(oldVersion) != 0):
             output += "(" + oldVersion + ")"
         if (len(newVersion) != 0):
             output += "[" + newVersion + "]"
         return output
    
    # retrieve the rest of the output array
    idxO = bestMatch[0]
    idxN = bestMatch[1]

    #recursive call on the remaining parts of the strings
    output += displayDiff(oldVersion[0:idxO], newVersion[0:idxN], depth)
    output += oldVersion[idxO:idxO + matchLen] 
    output += displayDiff(oldVersion[idxO+matchLen:], newVersion[idxN + matchLen:], depth)

    if (depth == 1):
        print ("stringDiff of : '" + oldVersion + "' and '" + newVersion + "' is:")
        print " '" + output + "'"

    return output
# end displayDiff

#    var output = code.displayDiff("a2_3b42c_78d", "a_34c27_8ed");
#    Console.WriteLine("a(2)_3(b)4(2)c(_)[2]7[_]8[e]d");

string1 = "a" #raw_input("Enter old string: ")
string2 = "b" #raw_input("Enter new string: ")
output = displayDiff(string1, string2,0)

string1 = "ab" #raw_input("Enter old string: ")
string2 = "ab" #raw_input("Enter new string: ")
output = displayDiff(string1, string2,0)

string1 = "CodeFights" #raw_input("Enter old string: ")
string2 = "ab" #raw_input("Enter new string: ")
output = displayDiff(string1, string2,0)

string1 = "dasdf" #raw_input("Enter old string: ")
string2 = "asdfd" #raw_input("Enter new string: ")
output = displayDiff(string1, string2,0)


string1 = "a2_3b42c_78d" #raw_input("Enter old string: ")
string2 = "a_34c27_8ed" #raw_input("Enter new string: ")
output = displayDiff(string1, string2,0)

string1 = "samePrefix_12333_syuffix" #raw_input("Enter old string: ")
string2 = "samePrefix12312333_sxuffix" #raw_input("Enter new string: ")
output = displayDiff(string1, string2,0)

# TODO: add to python repository