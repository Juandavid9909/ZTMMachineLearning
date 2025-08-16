is_old = True
is_licensed = True

if is_old and is_licensed:
    print('you are old enough to drive, and you have a license!')
else:
    print('you are not of age')
    
# Ternary operator
is_friend = False
can_message = 'message allowed' if is_friend else 'not allowed to message'

print(can_message)

# Operators => < > == >= <= != and or not
print(not(False))

# is operator - verifies if the value is the same object in memory
print(True == 1) # True
print(True is 1) # False