# Scope Notes 
# 1. Code in the global scope cannot use any local variables 
# 2. Code in a local scope can access global variables 
# 3. Code in one function's local scope cannot use variables in another local scope


def spam():
    global eggs # makes eggs a global scope variable 
    eggs = 'Hello' # assigns eggs variable globally
    print(eggs)

eggs = 42
spam() #function call 
print(eggs) # prints global eggs variable assigned within spam function