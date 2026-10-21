def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

def main():
    number = int(input("Enter an integer: "))
    result = check_even_odd(number)
    print(result)
    

if __name__=="__main__":
    main()