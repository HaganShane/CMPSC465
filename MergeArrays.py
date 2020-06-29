### Merge on page 51 on textbook ###
### Problem 7 on Rosalind ###

def merge():
    # read Rosalind dataset from txt file into arrays and their lengths
    # readline(): will return line from our file
    # strip(): strips any spaces at start or end
    # split(): splits our string into list
    with open("merge.txt") as mergeInput:
        arr1Size = int(mergeInput.readline().strip())
        arr1 = [int(a) for a in mergeInput.readline().split()]
        arr2Size = int(mergeInput.readline().strip())
        arr2 = [int(a) for a in mergeInput.readline().split()]

    merged = [] # declare merged list of arrays
    # extend(): extends array by adding items to the end
    # append(): adds one item to the end of array
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

# main function call
mergedFinal = merge()

# write answer to output.txt file (easier for the amount of numbers in given dataset)
with open("output.txt", "w") as outputFile:
    outputFile.write(' '.join([str(b) for b in mergedFinal]))

# check output.txt for answer, copy and paste into Rosalind
# attach python file below answer box
