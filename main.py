def bubble_sort():
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a

user_input = input("enter number separeted by spaces: ")
list_a = [int(num) for num in user_input.split()]
result = bubble_sort()

print("ordered numbers: ", result)