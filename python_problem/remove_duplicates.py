def remove_duplicates(numbers):
    unique_numbers = []
    
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
            
    return unique_numbers

def main():
    user_input = input("Enter numbers separated by spaces: ")
    
    numbers = [int(number) for number in user_input.split()]
    
    result = remove_duplicates(numbers)
    print("Orginal list:", numbers)
    print("Without duplicates:", result)
    
if __name__ == "__main__":
    main()