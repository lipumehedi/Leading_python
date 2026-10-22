def find_second_largest(numbers):
    largest = None
    second_largest = None
    
    for number in numbers:
        if largest is None or number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (second_largest is None or number > second_largest):
            second_largest = number
            
    if second_largest is None:
        return None
    return second_largest
    
def main():
    user_input = input("Enter numbers separated by spaces: ")
    
    try:
        numbers = [int(number) for number in user_input.split()]
        
        if not numbers:
            print("Error: Please enter at least two different numbers.")
            return
        result = find_second_largest(numbers)
        
        if result is None:
            print("Error: At least two different numbers are required.")
            
        else:
            print("second largest number:", result)
    except ValueError:
        print("Error: Please enter integers only.")
        
if __name__ == "__main__":
    main()
            