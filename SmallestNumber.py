def find_smallest_number(lst):
    smallest = lst[0] # initialize the smallest number as the first element of the list
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

list1 = [5, 7, 9, 14, 10, 20, 4]
print("The smallest number in list1 is:", find_smallest_number(list1))
