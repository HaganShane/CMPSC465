### Heaps described on page 114/115 of textbook ###
### Problem 18 on Rosalind ###
### Use code from building a heap (problem 11) ###

# "Sift-down" the new root element to its proper place.
def siftDown(array,arraySize, y):
    while True:
        # refer to return: on rosalind for 2<=i....
        node = y
        if (y*2) + 1 < arraySize and array[(y*2) + 1] > array[node]:
            node = (y*2) + 1
        # same as above, instead incriment another 1    
        if (y*2) + 2 < arraySize and array[(y*2) + 2] > array[node]:
            node = (y*2) + 2
        # once equal, break and do the swap 
        if node == y:
            break
        # swap
        array[y], array[node] = array[node], array[y]
        y = node

def buildHeap(array):
    # from build heap problem 11
    for x in range(arraySize - 1, 0, -1):
        parentNode = (x-1) // 2
        if array[x] > array[parentNode]:
            # swap
            array[parentNode], array[x] = array[x], array[parentNode]
            siftDown(array, arraySize, x)

# new function, same as above with different range and swaps
def sortheap(array):
    buildHeap(array)
    for z in range(arraySize, 1, -1):
        array[0], array[z - 1] = array[z - 1], array[0]
        siftDown(array, z - 1, 0)


def main():
    # call the new sortheap function
    sortheap(array)

    # write out to output.txt file for copy / paste answer into rosalind
    with open("output.txt", "w") as outputFile:
        outputFile.write(' '.join([str(b) for b in array]))

# read from rosalind dataset into array
with open("heapsort.txt") as heapSortInput:
    arraySize = int(heapSortInput.readline().strip())
    array = [int(a) for a in heapSortInput.readline().split()]    

# run the main function to call other functions
main()


# worked for sample dataset, try downloading and completing

