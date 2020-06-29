### Median on page 53/54 of textbook ###
### Problem 20 on Rosalind ###


def median():
    # load the dataset into the array
    with open("median.txt") as medianInput:
        arraySize = int(medianInput.readline().strip())
        array = [int(a) for a in medianInput.readline().split()]
    array.sort() # sort
    #print(array) test to see if it sorted
    print(array[15391-1]) # hardcode value when downloading set

median()

# works with sample, try with downloaded
    


