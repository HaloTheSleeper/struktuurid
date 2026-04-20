def heapify(arr, i, N):
    highest = i
    l = highest * 2 + 1
    r = highest * 2 + 2
    
    if l < N and arr[l] > arr[highest]:
        highest = l
    if r < N and arr[r] > arr[highest]:
        highest = r
    
    if i != highest:
        arr[i], arr[highest] = arr[highest], arr[i]
        
        heapify(arr, highest, N)
    
    
def heapSort(arr):
    #creating a max heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))
    print(arr)
    #moving root elements (max elements) out of the max heap to create a sorted array, where a[i] =< a[n]
    for i in range(len(arr) -1, -1, -1):
        print(i)
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

if __name__ == '__main__':
    arr = [12, 11, 10, 13, 5, 6, 8, 20, 7]

    # Function call
    heapSort(arr)
    
    N = len(arr)
    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")