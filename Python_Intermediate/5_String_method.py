
'''
Python String Methods

text = "Hello World"
1. lower() — সব ছোট হাতের অক্ষর
print(text.lower())

Output: hello world

2. upper() — সব বড় হাতের অক্ষর
print(text.upper())

Output: HELLO WORLD

3. capitalize() — প্রথম অক্ষর বড়
text = "hello world"

print(text.capitalize())

Output: Hello world

4. title() — প্রতিটি word-এর প্রথম অক্ষর বড়
text = "hello world"

print(text.title())

Output: Hello World

5. strip() — দুই পাশের extra space remove
text = "   Hello World   "

print(text.strip())

Output: Hello World

6. lstrip() — বাম পাশের space remove
text = "   Hello World"

print(text.lstrip())

7. rstrip() — ডান পাশের space remove
text = "Hello World   "

print(text.rstrip())

8. replace() — text পরিবর্তন করা
text = "Hello World"

print(text.replace("World", "Python"))

Output: Hello Python

9. find() — কোনো text কোথায় আছে খুঁজে বের করা
text = "Hello World"

print(text.find("World"))

Output: 6
কারণ World index 6 থেকে শুরু হয়েছে।

10. count() — কতবার আছে
text = "Python is easy. Python is powerful."

print(text.count("Python"))

Output: 2

11. startswith() — নির্দিষ্ট text দিয়ে শুরু কিনা
text = "Hello World"

print(text.startswith("Hello"))

Output: True

12. endswith() — নির্দিষ্ট text দিয়ে শেষ কিনা
text = "Hello World"

print(text.endswith("World"))

Output: True

13. isdigit() — শুধু number কিনা
text = "12345"

print(text.isdigit())

Output:  True

কিন্তু: text = "123abc"

print(text.isdigit())

Output: False

14. isalpha() — শুধু alphabet কিনা
text = "Python"

print(text.isalpha())

Output: True

কিন্তু: text = "Python123"

print(text.isalpha())

Output:False

15. isalnum() — alphabet অথবা number
text = "Python123"

print(text.isalnum())

Output: True

কিন্তু space থাকলে:

"Python 123".isalnum()

Output: False

16. isspace() — শুধু space কিনা
text = "   "

print(text.isspace())

Output: True
'''