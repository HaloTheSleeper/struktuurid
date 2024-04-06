#quicksort random pivot selecting and using insertion sort when the subarray is shorter than 7 units/spaces
#work in progress
import random

def partition(arr, low, high):
    pivotIndex = random.randrange(low, high)
    pivot = arr[pivotIndex]
    
    i, j = low - 1, low
    
    while (j <= high):
        if arr[j] < arr[pivotIndex]:
            i += 1
            
            if j == pivotIndex:
                pivotIndex = i
            elif i == pivotIndex:
                pivotIndex = j
            
            (arr[j], arr[i]) = (arr[i], arr[j])
            
        j += 1
        
    arr[i + 1], arr[pivotIndex] = arr[pivotIndex], arr[i + 1]    
     
    return i + 1     
    
    #doesnt change the actual array
    """   left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    arr = left + middle + right """



    

def quicksort(arr, low, high):
    if low >= high:
        return

    pi = partition(arr, low, high)
    
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)


array = [7, 5, 9, -3, 4, 2, 100]

quicksort(array, 0, len(array) - 1)

print(array)