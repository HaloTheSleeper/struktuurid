def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:

            i += 1

            (arr[i], arr[j]) = (arr[j], arr[i])
        
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1


def quicksort(arr, low, high):
    if (low > high):
        return
    
    pi = partition(arr, low, high)

    quicksort(arr, low, pi - 1)

    quicksort(arr, pi + 1, high)


array = [1, 5, 9, -3, 2, 100]

quicksort(array, 0, len(array) - 1)

print(array)