# Global
total = 0

def count():
    global total
    total += 1
    
    return total

count() # 1
count() # 2

# Nonlocal
def outer():
    x = 'local'
    
    def inner():
        nonlocal x
        x = 'nonlocal'
        
        print('inner:', x) # nonlocal
        
    inner()
    
    print('outer:', x) # nonlocal
    
outer()