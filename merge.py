def merge_sort(array):
    if len(array) <=1:
        return array


    mid = len(array)//2
    left_half = array[:mid]
    right_half = array[mid:]