# Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # find the index of the next smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # swap the elements
        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# Implement the Bubble Sort function below
def bubble_sort(arr):

    sorting = True

    while sorting:
        sorting = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorting = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr