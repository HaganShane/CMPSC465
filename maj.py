### Majority element descirbed on Rosalind site ###
### An array A[1...n] is said to have a majority element if more than half of its entries are the same ###
### Problem 6 on Rosalind ###

# create a function to find the majority element in given array
def majElem():
    # read in the array from txt file
    # need to copy and paste each individual array into file
    # cant figure out how to read each array
    with open("majElem.txt") as majElemInput:
        array = [int(a) for a in majElemInput.readline().split()]

    size = len(array) # get size of the array
    totalCount = [0] * ((10**4) + 1) # n <= 10^4
    half = size / 2 # mark half of the size first to satisfy majority element condition

    # loop through to see if majority element, if so, return the majority element
    for x in array:
        totalCount[x] += 1
        if totalCount[x] > half:
            return x
                
    # if not a majority element, output -1
    return -1
    


# run / print the value to terminal
# will have to copy / paste each array into input file
print(majElem())



# worked on each array in sample, try download now
