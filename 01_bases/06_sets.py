my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set) # {1, 2, 3, 4, 5, 100}
print(1 in my_set)

new_set = my_set.copy()
print(list(new_set)) # [1, 2, 3, 4, 5, 100]