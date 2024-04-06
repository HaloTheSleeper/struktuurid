def partition(arr, low, high):
    pivot = arr[low] 
    
    start = low + 1
    end = high
    
    while True:
        # peatub kuni leiab algusest indexi, millel olev vaartus on pivotist suurem
        while end >= start and arr[start] <= pivot:
            start += 1
        # peatub kuni leiab lopust indexi, millel olev vaartus on pivotist vaiksem
        while end >= start and arr[end] >= pivot:
            end -= 1  
        
        if start <= end:
            #vahetame ara algusest leitud suure vaartuse ja lopust leitud vaikese
            arr[start], arr[end] = arr[end], arr[start]
        else: 
            break
        
    arr[low], arr[end] = arr[end], arr[low]
    
    return end
        
        


def quicksort(arr, low, high):
    if low >= high:
        return
 
    pivotLen = partition(arr, low, high)

    quicksort(arr, low, pivotLen - 1)
    quicksort(arr, pivotLen + 1, high)


array = [1, 5, 9, -3, 2, 2, 100]

quicksort(array, 0, len(array) - 1)

print(array)



"""
    # First Element as pivot
    pivot = arr[low]
    
    start = low + 1
     
    # end points to the ending of the array
    end = high
 
    while True:
        # It indicates we have already moved all the elements to their correct side of the pivot
        while start <= end and arr[end] >= pivot:
            end = end - 1
 
        # Opposite process
        while start <= end and arr[start] <= pivot:
            start = start + 1
 
        # Case in which we will exit the loop
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            # The loop continue
        else:
            # We exit out of the loop
            break
 
    arr[low], arr[end] = arr[end], arr[low]
    # As we got pivot element index is end
    # now pivot element is at its sorted position
    # return pivot element index (end)
    return end """