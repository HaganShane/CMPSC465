### Insertion sort pseudo code on Rosalind page ###
### Problem 4 on Rosalind ###

# From link on Rosalind Site: http://www.sorting-algorithms.com/insertion-sort
# for i = 2:n,
#    for (k = i; k > 1 and a[k] < a[k-1]; k--)
#        swap a[k,k-1]
#    → invariant: a[1..i] is sorted
# end

def insertionSort():
    # read from rosalind dataset into our array
    with open("insertionSort.txt") as insertionSortInput:
        arraySize = int(insertionSortInput.readline().strip())
        array = [int(a) for a in insertionSortInput.readline().split()]

    count = 0
    # for loop to run through the entire array
    for x in range(1, arraySize):
        k = x
        # use above pseudo, increment k at end of while loop
        while (k >= 1) and (array[k] < array[k-1]):
            # swap the array[k] and array[k-1] per psuedo
            array[k-1], array[k] = array[k], array[k-1]
            count += 1 # increment count by 1
            k -= 1 # increment k by -1
    return count

# print out of final value (answer) for the number of swaps performed
print(insertionSort())

# worked for sample dataset (12), try with new dataset
            
        
