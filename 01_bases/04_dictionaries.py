dictionary = {
    'a': 1,
    'b': 2
}

user2 = dict(name='JohnJohn')
print(dictionary['b'])
print(user2)

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('greet' in user.keys())
print('hello' in user.values())
print(user.update({'ages': 55}))