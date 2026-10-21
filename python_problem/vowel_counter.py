def count_vowels(text):
    vowels = "aeiou"
    count = 0
    
    for char in text.lower():
        if char in vowels:
            count += 1
            
    return count


def main():
    text = input("Enter a sentence: ")
    result = count_vowels(text)
    
    print("Number of vowels:", result)
    
if __name__== "__main__":
    main()