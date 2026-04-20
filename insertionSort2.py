# reverse bubblesort, lesssgooo
def insertionSort(arr):
    n = len(arr)
    
    for i in range(1, n):
        j = i
        while (j >= 1 and arr[j] < arr[j - 1]):
            (arr[j], arr[j - 1]) = (arr[j - 1], arr[j])
            j -= 1
        
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])