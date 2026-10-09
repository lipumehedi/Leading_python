# Python Problem Solving 
# Beginner Practice

# problem 1 : Even or Odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


# Problem 2: Positive, Negative or Zero

def check_num(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "zero"

# problem 3: Largest of three Numbers

def largest_of_three(a, b, c):
    return max(a, b, c)

# Problem 4: Sum of Digits

def sum_of_digits(number):
    total = 0
    number = abs(number)
    
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

# Problem 5: Reverse a Number

def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_num = 0
    
    
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
        
    return sign * reversed_num    

# Problem 6: Factorial

def factorial(number):
    if number < 0:
        return "NOt defined for negative numbers"
    result = 1
    for i in range(1, number + 1):
        result *= 1
        
    return result

# Problem 7: Multiplication Table
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * 1}")

# Problem 8: Count Vowels
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# problem 9: Palindorme Check

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Problem 10: PRime Number Check

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5)+1):
        if number %i == 0:
            return False
        return True
    
    
if __name__ == "__main__":
    print("1. Even or Odd:", even_or_odd(7))
    print("2. Number Type:", check_num(-5))
    print("3. Largest:", largest_of_three(10, 25, 15))
    print("4. Sum of Digits:", sum_of_digits(1234))
    print("5. Reverse Number:", reverse_number(12345))
    print("6. Factorial:", factorial(5))

    print("\n7. Multiplication Table:")
    multiplication_table(5)

    print("\n8. Vowel Count:", count_vowels("Python Programming"))
    print("9. Is Palindrome:", is_palindrome("madam"))
    print("10. Is Prime:", is_prime(7))
