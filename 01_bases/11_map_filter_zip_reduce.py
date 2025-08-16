from functools import reduce

# Map
my_list = [1, 2, 3]

def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, my_list))) # [2, 4, 6]
print(my_list) # [1, 2, 3]

# Filter
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list))) # [1, 3]
print(my_list) # [1, 2, 3]

# Zip
your_list = (10, 20, 30)
their_list = (5, 4, 3)

print(list(zip(my_list, your_list, their_list))) # [(1, 20, 5), (2, 20, 4), (3, 30, 3)]
print(my_list) # [1, 2, 3]

# Reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10)) # 10 1 -> 11 2 -> 13 3 -> 16
print(my_list) # [1, 2, 3]