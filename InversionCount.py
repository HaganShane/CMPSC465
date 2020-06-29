### Counting Inversions ###
### Problem 19 on Rosalind ###

def countInversion():
    # read from rosalind dataset into our array
    with open("countInversion.txt") as countInversionInput:
        arraySize = int(countInversionInput.readline())
        array = [int(a) for a in countInversionInput.readline().split()]
    inversionCount = 0 # set the count equal to 0 to start
    for b in range(arraySize):
        for c in range(b + 1, arraySize):
            # increment 1 to inversionCount if previous value larger than next
            if(array[b] > array[c]): 
                inversionCount += 1
    print(inversionCount)

countInversion()

# worked for sample dataset (2), try download dataset
# slow for first couple datasets




    
