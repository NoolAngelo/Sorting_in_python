def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
    return list_a

# Get user input for the list of numbers
numbs = input("Input numbers, separated with spaces: ")

# Convert the input string into a list of integers
numbers =[int(num) for num in numbs.split()]

sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)
