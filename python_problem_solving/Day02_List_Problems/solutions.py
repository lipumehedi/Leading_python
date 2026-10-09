
# Python Problem Solving - Day 02
# List Problems

# Problem 1: Sum of List Elements
def sum_of_list(numbers):
    total = 0
    i = 0

    while i < len(numbers):
        total += numbers[i]
        i += 1

    return total


# Problem 2: Find Maximum Number
def find_maximum(numbers):
    maximum = numbers[0]
    i = 1

    while i < len(numbers):
        if numbers[i] > maximum:
            maximum = numbers[i]
        i += 1

    return maximum


# Problem 3: Find Minimum Number
def find_minimum(numbers):
    minimum = numbers[0]
    i = 1

    while i < len(numbers):
        if numbers[i] < minimum:
            minimum = numbers[i]
        i += 1

    return minimum


# Problem 4: Count Even and Odd Numbers
def count_even_odd(numbers):
    even = 0
    odd = 0
    i = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            even += 1
        else:
            odd += 1
        i += 1

    return even, odd


# Problem 5: Reverse a List
def reverse_list(numbers):
    reversed_numbers = []
    i = len(numbers) - 1

    while i >= 0:
        reversed_numbers.append(numbers[i])
        i -= 1

    return reversed_numbers


# Problem 6: Search an Element
def search_element(numbers, target):
    i = 0

    while i < len(numbers):
        if numbers[i] == target:
            return "Found"
        i += 1

    return "Not Found"


# Problem 7: Count Positive Numbers
def count_positive(numbers):
    count = 0
    i = 0

    while i < len(numbers):
        if numbers[i] > 0:
            count += 1
        i += 1

    return count


# Problem 8: Remove Duplicates
def remove_duplicates(numbers):
    unique_numbers = []
    i = 0

    while i < len(numbers):
        if numbers[i] not in unique_numbers:
            unique_numbers.append(numbers[i])
        i += 1

    return unique_numbers


# Problem 9: Find Second Largest
def second_largest(numbers):
    unique_numbers = remove_duplicates(numbers)

    if len(unique_numbers) < 2:
        return None

    largest = unique_numbers[0]
    second = None
    i = 1

    while i < len(unique_numbers):
        number = unique_numbers[i]

        if number > largest:
            second = largest
            largest = number
        elif second is None or number > second:
            second = number

        i += 1

    return second


# Problem 10: Calculate Average
def calculate_average(numbers):
    if len(numbers) == 0:
        return None

    total = sum_of_list(numbers)
    return total / len(numbers)


# Test All Problems
if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    values = [12, 45, 7, 89, 23]
    mixed = [-2, 5, 0, 8, -1, 3]

    print("1. Sum:", sum_of_list(numbers))
    print("2. Maximum:", find_maximum(values))
    print("3. Minimum:", find_minimum(values))

    even, odd = count_even_odd([1, 2, 3, 4, 5, 6])
    print("4. Even:", even, "Odd:", odd)

    print("5. Reverse:", reverse_list([1, 2, 3, 4, 5]))
    print("6. Search:", search_element(numbers, 30))
    print("7. Positive Count:", count_positive(mixed))
    print("8. Remove Duplicates:",
          remove_duplicates([1, 2, 2, 3, 3, 4]))

    print("9. Second Largest:",
          second_largest([10, 25, 8, 40, 30]))

    print("10. Average:", calculate_average(numbers))
