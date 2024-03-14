def merge_sort(array):
    if len(array) <=1:
        return array


    mid = len(array)//2
    left_half = array[:mid]
    right_half = array[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left,right):
    merged =[]
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index +=1
        else:
            merged.append((right[right_index]))
            right_index +=1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])\

    return merged

user_input = input("Enter numbers comma separated: ")
array = list(map(int, user_input.split(',')))

print(" ")
print("unsorted list: ", (array))
print("length of the list is: ",len(array))
print("sorted list: ", merge_sort(array))
if (len(array) % 2) == 0:
    print("the array is even")
else:
    print("the array is odd")
