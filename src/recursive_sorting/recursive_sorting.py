# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    for i in range(0, elements):
      if len(arrA) == 0:
        merged_arr[i] = arrB[0]
        arrB = arrB[1:]
      elif len(arrB) == 0:
        merged_arr[i] = arrA[0]
        arrA = arrA[1:]
      elif arrA[0] < arrB[0]:
        merged_arr[i] = arrA[0]
        arrA = arrA[1:]
      elif arrB[0] < arrA[0]:
        merged_arr[i] = arrB[0]
        arrB = arrB[1:]    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    half = len(arr) // 2
    if len(arr) > 1:
      return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))
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
