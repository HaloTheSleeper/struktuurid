def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        j = i
        while (j < n - 2 and arr[j] > arr[j + 1]):
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
                j += 1
                swapped = True
            
        if (swapped == False):
            return



arr = [12, 34, 25, 36, 22, 11, 90]

bubbleSort(arr)
print(arr)
