print("Hello! Welcome to my program! :)")

user_number = int(input("Enter a number to be multiplied by 3: "))

def mult(number): 
    result = number * 3 
    return result

print("The answer is %s " % mult(user_number))

first_number = int(input("Now, enter a new number: "))

second_number = int(input("And another one to be added to the previous: "))

def add(a, b): 
    result = a + b 
    return result

print("The answer is %s " % add(first_number, second_number))

print("Great! Let´s end by creating a list of 3 integers in order to find the sum of them.")

listOfNumbers = []

while len(listOfNumbers) < 3:
    item = input("Enter a number: ")
    listOfNumbers.append(int(item))
    print(listOfNumbers)

def sumOfNumbers(listOfNumbers):
    sum = listOfNumbers[0] + listOfNumbers[1] + listOfNumbers[2]
    print("The answer is %s " % sum)

sumOfNumbers(listOfNumbers)

print("Thank you for your inputs!")

