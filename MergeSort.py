### Merge Sort and Merge psuedo code on pages 50/51 ###
### Problem 12 of Rosalind ###

### Use part of merge() from problem 7 of Rosalind to help with this ###

def mergeSort(array):
    arrayLength = len(array)
    mid = round(arrayLength / 2)
    # reverse of page 50 mergesort function
    if mid < 1:
        return array
    # capture right half of array
    rightArray = array[mid:]
    rightArray = mergeSort(rightArray)
    # capture left half of array
    leftArray = array[:mid]
    leftArray = mergeSort(leftArray)

    finalArray = merge(leftArray, rightArray)
    return finalArray

# now use the merge() function from previous problem 7
def merge(arr1, arr2): # update this to take in the two arrays as arguments
    merged = [] # declare merged list of arrays
    # extend(): extends array by adding items to the end
    # append(): adds one item to the end of array
    # pop(): remove indexed item, then return the item
    while (arr1 or arr2):
        if not arr1:
            merged.extend(arr2)
            return merged
        elif not arr2:
            merged.extend(arr1)
            return merged
        elif arr1[0] <= arr2[0]: # from textbook function merge
            merged.append(arr1.pop(0))
        else: # from textbook function merge
            merged.append(arr2.pop(0))

    return merged

# finally add function to easily read in values to array
# and also write out to the output.txt file for easy copy / paste to rosalind
# code taken / modified from rest of merge() code from problem 7
def fileHandling():
    with open("mergeSort.txt") as mergeSortInput:
        arraySize = int(mergeSortInput.readline().strip())
        array = [int(a) for a in mergeSortInput.readline().split()]

    finalMerged = mergeSort(array) # call mergeSort to sort array after file call

    with open("output.txt", "w") as outputFile:
        outputFile.write(' '.join([str(b) for b in finalMerged]))
    return finalMerged
    

# call to run function and have it output to file for our final answer    
fileHandling()
# passed sample dataset check, run on real dataset
