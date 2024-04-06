def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = len(arr) // 2
    
    left = [x for x in arr if x < arr[pivot]]
    middle = [x for x in arr if x == arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return quicksort(left) + middle + quicksort(right)


array = [1, 7, 4, 1, 10, 9, 5]
if __name__ == '__main__':
    print(quicksort(array))