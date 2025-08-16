my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set) # {1, 2, 3, 4, 5, 100}
print(1 in my_set)

new_set = my_set.copy()
print(list(new_set)) # [1, 2, 3, 4, 5, 100]

# Methods
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set.difference(your_set)) # {1, 2, 3}

my_set.discard(5)
print(my_set) # {1, 2, 3, 4}

my_set.difference_update(your_set)
print(my_set) # {1, 2, 3}

print(my_set.intersection(your_set)) # {4, 5} - (my_set & your_set) is the same

print(my_set.isdisjoint(your_set)) # True if they have elements in common

print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - (my_set | your_set) is the same

my_set = {4, 5}
print(my_set.issubset(your_set)) # True

print(your_set.issuperset(my_set)) # False - The same as the previous example but verifying we have the elements inside the set