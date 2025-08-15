li = [1, 2, 3, 4, 5]

# Slicing
new_cart = li[0:3]

# Matrix
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]

print(matrix[0][1])

# Methods
basket = [1, 2, 3, 4, 5]
basket.append(100) # [1, 2, 3, 4, 5, 100]
basket.insert(4, 100) # [1, 2, 3, 100, 4, 5, 100]
basket.extend([101]) # [1, 2, 3, 100, 4, 5, 100, 101]
basket.pop() # [1, 2, 3, 100, 4, 5, 100]
basket.pop(0) # [2, 3, 100, 4, 5, 100]
basket.clear() # []

basket = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d', 0, 2)) # 2 last parameters are optional, and are start and end for our search
print('x' in basket) # False
basket.count('d') # 2
basket.sort()
sortedList = sorted(basket) # Returns a new sorted list
basket.reverse()

copiedList = basket.copy() # Creates a shallow copy of the list

len(basket) # 6 - length of the list

print(list(range(1, 100))) # Create a list from 1 to 100

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO']) # hi my name is JOJO