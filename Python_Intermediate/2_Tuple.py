'''
Python Tuple

locked, immutable. limiting,

ordered - yes
changeable - no
 duplicate - yes
syntax - ()


Access by index — exactly like a list '''
colour = (255, 165, 0)  # Red, Green, Blue
print(colour[0])    # 255 — Red
print(colour[-1])   # 0   — Blue (last)
print(colour[0:2])  # (255, 165) — slicing works too

if 255 in colour:
    print("Max red!")


#Unpacking a Tuple
#Assign each value to its own variable in one line
#One of Python's most loved features. Instead of [0], [1], [2] — name each value directly:

colour = (255, 165, 0)
red, green, blue = colour       # unpack!
print(red, green, blue)        # 255  165  0

# Swap two variables using tuple magic
a, b = 10, 20
a, b = b, a                    # a=20, b=10 — no temp variable needed!

# Functions return multiple values as a tuple
def get_size():
    return 1920, 1080          # returns a tuple
width, height = get_size()
print(f"{width}x{height}")


#.count(x)	Count how many times x appears	(1,2,2,3).count(2) → 2
#.index(x)	Find position of first x	(10,20,30).index(20) → 1
