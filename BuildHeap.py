### Heaps described on page 114/115 of textbook ###
### Problem 11 on Rosalind ###

def buildHeap():
    # read from rosalind dataset into array
    with open("buildHeap.txt") as buildHeapInput:
        arraySize = int(buildHeapInput.readline().strip())
        array = [int(a) for a in buildHeapInput.readline().split()]

    for x in range(arraySize - 1, 0, -1):
        parentNode = (x-1) // 2
        if array[x] > array[parentNode]:
            # swap
            array[parentNode], array[x] = array[x], array[parentNode]

            # equal to our for loop variable 
            y = x
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
    # write out to output.txt file for copy / paste answer into rosalind
    with open("output.txt", "w") as outputFile:
        outputFile.write(' '.join([str(b) for b in array]))
        
# run the function
buildHeap()


# worked for sample dataset, try downloading and completing

