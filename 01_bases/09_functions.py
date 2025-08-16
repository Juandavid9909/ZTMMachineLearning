def say_hello(first_name, last_name):
    print(f'hello {first_name} {last_name}')
    
say_hello('John', 'Doe')

# Default parameters and Keyword arguments
def say_hello2(first_name = 'Darth', last_name = 'Vader'):
    print(f'hello {first_name} {last_name}')
    
say_hello2(name = 'Bibi', last_name = 'Fett')

# *args and **kwargs
# Rule: params, *args, default parameters, **kwargs
def super_func(name, *args, i = 'hi', **kwargs):
    total = 0
    
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('Andy', 1, 2, 3, 4, 5, num1 = 5, num2 = 10))