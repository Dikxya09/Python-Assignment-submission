#function that takes a number as input and returns whether it is even or odd.
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#function that takes two numbers and an operator (+, -, *, /) and returns the result of the operation.
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

#function that returns the largest among three given numbers.
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
#function that counts and returns the number of vowels in a given string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

#function that accepts a list of numbers and returns only the positive numbers in a new list
def filter_positive_numbers(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers

#function to compute the factorial of a given number using a loop.
def factorial(n):
    if n < 0:
        return "Factorial of negative number is undefined"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#function that checks whether a given string is a palindrome
def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

#function that prints a right-angled triangle pattern of * based on the number of rows provided
def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end='')
        print()  # Move to the next line after each row

#function that returns the sum of all elements in a list of numbers
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#function that takes a name and time of day (morning, afternoon, evening) and returns a suitable greeting
def greet(name, time_of_day):
    if time_of_day.lower() == 'morning':
        return f"Good morning, {name}!"
    elif time_of_day.lower() == 'afternoon':
        return f"Good afternoon, {name}!"
    elif time_of_day.lower() == 'evening':
        return f"Good evening, {name}!"
    else:
        return f"Hello, {name}!" 