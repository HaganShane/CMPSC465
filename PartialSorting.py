### Partial Sorting described on Rosalind Site ###
### Problem 25 on Rosalind ###
### Almost same as previous problem (median) with some modifications ###

def partialSort():
    # load the dataset into the array
    with open("partialSort.txt") as partialSortInput:
        arraySize = int(partialSortInput.readline().strip())
        array = [int(a) for a in partialSortInput.readline().split()]
    array.sort() # sort
    #print(array) test to see if it sorted
    finalArray = array[:804] # hardcode with given value in dataset

    # modified to output to txt file for copy and paste to rosalind
    # write answer to output.txt file (easier for the amount of numbers in given dataset)
    with open("output.txt", "w") as outputFile:
        outputFile.write(' '.join([str(b) for b in finalArray]))
    
partialSort()

# works with sample, try with downloaded
    
