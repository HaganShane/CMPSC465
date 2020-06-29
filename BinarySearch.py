### Binary Search on page 50 ###
### Problem 2 on Rosalind ###

def binarySearch():
    # read arrays from binSearch.txt file (easier for the amount of numbers in given dataset)
    with open("binSearch.txt", "r") as binSearch:
        len1 = int(binSearch.readline())
        len2 = int(binSearch.readline())
        arr1 = [int(x) for x in binSearch.readline().split()]
        arr2 = [int(x) for x in binSearch.readline().split()]
    answer = [] # Final answer output array

    for arr2mid in arr2:
        mid = round(len1 / 2) # middle of array
        bottom = 0 # bottom of array, 0 index
        top = len1
        while (bottom < mid < top) and arr2mid != arr1[mid]:
            if (arr2mid < arr1[mid]):
                top = mid
                mid = round((bottom + top) / 2)
            elif (arr2mid > arr1[mid]):
                bottom = mid 
                mid = round((bottom + top) / 2)
        else:
            if arr2mid == arr1[mid]:
                answer.append(mid + 1) # add values to answer array
            else:
                answer.append(-1) # add -1 to answer array if 'no such index'

    # write answer to output.txt file (easier for the amount of numbers in given dataset)
    with open("output.txt", "w") as outputFile: 
        outputFile.write(' '.join([str(x) for x in answer])) 

    return # return successfully

binarySearch() # run the program

# will have to type something in upon run
