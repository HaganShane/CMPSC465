### Quick Sort description on page 56 of textbook ###
### Problem 29 on Rosalind ###
### Quick sort pseudocode ###
'''
def quicksort(array[1...n]):
    choose random x from {1...n}
    y = array[x]
    array_s, array_z, array_y = split(array[1...n], y)
    quicksort(array_s)
    quicksort(array_z)
'''
### More pseudocode taken from 'visualization' site off rosalind problem ###
'''
_# choose pivot_
swap a[n,rand(1,n)]

_# 3-way partition_
i = 1, k = 1, p = n
while i < p,
  if a[i] < a[n], swap a[i++,k++]
  else if a[i] == a[n], swap a[i,--p]
  else i++
end
_→ invariant: a[p..n] all equal_
_→ invariant: a[1..k-1] < a[p..n] < a[k..p-1]_

_# move pivots to center_
m = min(p-k,n-p+1)
swap a[k..k+m-1,n-m+1..n]

_# recursive sorts_
sort a[1..k-1]
sort a[n-p+k+1,n]
'''
### Resubmit, can't just use python sort() function ###
### Need to implement new code ###

# import random for the quicksort part
import random

# modified 3waypartition from other rosalind problem 
def threewaypart(array, start, end):
    # choose pivot
    pivotPoint = array[start]
    # set the left and right halves
    leftSide, rightSide = start, end
    # while the halves aren't equal
    while leftSide != rightSide:
        while rightSide != leftSide and array[rightSide] > pivotPoint:
            # incriment by -1
            rightSide -= 1
        # swap 
        array[leftSide], array[rightSide] = array[rightSide], array[leftSide]
        # same as above, but with left side
        while leftSide != rightSide and array[leftSide] <= pivotPoint:
            # incriment by +1
            leftSide += 1
        # swap again
        array[leftSide], array[rightSide] = array[rightSide], array[leftSide]
    return leftSide


# read input from rosalind dataset
with open("quicksort.txt") as quickSortInput:
    arraySize = int(quickSortInput.readline().strip())
    array = [int(a) for a in quickSortInput.readline().split()]

def quicksortAlgo(array, start = 0, end = None):
    # check the end and incriment accordingly
    if end == None:
        end = arraySize - 1
    if start > end:
        return

    # get random number (from above pseudo and swap)
    i = random.randrange(start, end + 1)
    array[start], array[i] = array[i], array[start]

    # use other functions, begin quick sort
    point = threewaypart(array, start, end)
    point2 = point + 1
    point3 = point - 1
    quicksortAlgo(array, start, point3)
    quicksortAlgo(array, point2, end)

    # write out to output.txt and copy / paste into rosalind solution
    with open("output.txt", "w") as outputFile:
        outputFile.write(' '.join([str(b) for b in array]))

# call the quicksort algorithm with array parameter
quicksortAlgo(array)


# worked on sample dataset, try downloading new dataset and resubmitting


