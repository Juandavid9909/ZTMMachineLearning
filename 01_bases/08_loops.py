# For loop
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)
        
# Range
for i in range(10, 0, 2):
    print(i)
    
# Enumerate
for i, char in enumerate(list(range(100))):
    print(i, char)
    
# While loop
i = 0
while i < 50:
    response = input('Say something: ')
    print(i)
    i += 1
else:
    print('done with all the work')