# Complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    
    # while both arrays have elements, compare the first element of each array
    for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.pop(0)

    return merged_arr


# Implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        arr_midpoint = len(arr)//2
        arrA = arr[:arr_midpoint]
        arrB = arr[arr_midpoint:]
        return merge(merge_sort(arrA), merge_sort(arrB))


    
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
