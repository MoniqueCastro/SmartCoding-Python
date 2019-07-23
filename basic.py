print("Hello! Welcome to my program! :)")

def mult(number): 
    result = number * 3 
    return result

print("The answer of the first operation is %s " % mult(3))

def add(a, b): 
    result = a + b 
    return result

print("The answer of the second operation is %s " % add(1, 3))

numbers = [1, 2, 3, 6]

def sumOfListNumbers(numbers): 
    sum = 0 
    for item in numbers: 
        sum += item
    return sum

print("The answer of the third operation is %s " % sumOfListNumbers(numbers))

assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4
