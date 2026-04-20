#quicksort random pivot selecting and using insertion sort when the subarray is shorter than 4 units/spaces
import random

def insertionSort(arr, low, high):
    i = low
    
    while (i < high):
        if (arr[i + 1] < arr[i]):
            #found smaller element
            smallerIndex = i + 1
            
            while (arr[smallerIndex] < arr[smallerIndex - 1] and smallerIndex > low):
                (arr[smallerIndex], arr[smallerIndex - 1]) = (arr[smallerIndex - 1], arr[smallerIndex])
        
                smallerIndex -= 1
        
        i += 1 
            
def partition(arr, low, high):
    pivotIndex = random.randrange(low, high)
    
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

def quicksort(arr, low, high):
    if low >= high:
        return
    
    if (high - low < 4):
        insertionSort(arr, low, high)
        return

    pi = partition(arr, low, high)
    
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)


array = [7, 5, 9, -3, 4, 2, 100]

quicksort(array, 0, len(array) - 1)

print(array)