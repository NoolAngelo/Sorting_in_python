def insertion():
    user_input = input("enter numbers separated with space: ")
    list_a = [int(num) for num in user_input.split()]

    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_ = list_a[i]

        while list_a[i-1] > value_ and i >0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i=i-1
    return list_a

result = insertion()
print("ordered list: ",result)
