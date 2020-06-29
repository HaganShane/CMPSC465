### 3-Way Partition described on Rosalind site ###
### Code used from previous 2-Way partition problem ###
### Problem 20 on Rosalind ###

def threeWayPart():
    # read from rosalind dataset into array
    with open("threewaypart.txt") as threewaypartInput:
        arraySize = int(threewaypartInput.readline().strip())
        array = [int(a) for a in threewaypartInput.readline().split()]

    less = [] # less than lamda
    equal = [] # equal to lamba
    greater = [] # greater than lamda

    value = array[0]
    for x in array:
        # cover case for if our value is equal to indexed value
        if x == value:
            equal.append(x)
        # cover case for if our value is less than indexed value
        elif x < value:
            less.append(x)
        # cover case for if our value is greater than indexed value
        else:
            greater.append(x)

    # put the list in order i.e., less, equal greater. sorts the list
    less.extend(equal)
    less.extend(greater)

    # write out to output.txt file for copy / paste answer into rosalind
    with open("output.txt", "w") as outputFile:
        outputFile.write(' '.join([str(b) for b in less]))

threeWayPart() # run the program
