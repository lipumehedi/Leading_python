def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

def main():
    text = input("Enter a word: ")
    
    if is_palindrome(text):
        print("Palindrome")
    else:
        print("Not Palindrome")
        
if __name__=="__main__":
    main()