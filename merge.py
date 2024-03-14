def merge_sort(array):
    if len(array) <=1:
        return array


    mid = len(array)//2
    left_half = array[:mid]
    right_half = array[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left,right):
