# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)

# The main function to sort an array of given size


def heapSort(arr):
    N = len(arr)

    # Build a maxheap.
    print(arr)
    for i in range(N//2 - 1, -1, -1):
        print(f"First {i}")
        heapify(arr, N, i)
        print(arr)
        
    print("##############")

    # One by one extract elements
    for i in range(N-1, 0, -1):
        print(f"Second {i}")
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        print(arr)


# Driver's code
if __name__ == '__main__':
    arr = [12, 11, 10, 13, 5, 6, 8, 20, 7]

    # Function call
    heapSort(arr)
    N = len(arr)

    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")
# This code is contributed by Mohit Kumra