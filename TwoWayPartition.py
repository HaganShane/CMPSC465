### 2-Way Partition described on Rosalind site ###
### Problem 13 on Rosalind ###

def twoWayPart():
    # read from rosalind dataset into array
    with open("twowaypart.txt") as twowaypartInput:
        arraySize = int(twowaypartInput.readline().strip())
        array = [int(a) for a in twowaypartInput.readline().split()]

    less = [] # less than lamda
    greater = [] # greater than lamda
    for x in range(1, arraySize):
        # cover case for if our value is less than indexed value
        if array[x] <= array[0]:
            less.append(array[x])
        # cover case for if our value is greater than indexed value
        else:
            greater.append(array[x])

    # put the list in order i.e., less, greater. sorts the list
    less.append(array[0])
    less.extend(greater)

    # write out to output.txt file for copy / paste answer into rosalind
    with open("output.txt", "w") as outputFile:
        outputFile.write(' '.join([str(b) for b in less]))

twoWayPart() # run the program
