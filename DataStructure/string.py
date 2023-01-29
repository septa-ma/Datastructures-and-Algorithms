# what is string?
# a data type in general and typically represented as arrays
# of bytes or words that store a sequence of characters.
# strings are defined as an array of characters.
# the difference between a character array and a string is
# the string is terminated with a special character ‘\0’.
# the string stors as a character array in memory, which has index.

# 1- Declare String in python
String1 = "Welcome to SEPTA world, hope it'll be useful for you."
String2 = 'Here you can improve or review your DS and Algorithm knowledg.'
print(String1)
print(String2)

# 2- Loop on a string
for letter in String1:
    print(letter)

for i in range(0, len(String2)):
    print(i, String2[i])

# 3- Sliceing a string -> string-name[start-index:end-index]
print(String2[:14])
print(String2[15:30])
print(String2[20:])
print(String2[-1]) # last character
print(String2[-10:-1])

# 4- Find or Search a character in string
print('Algorithm' in String2) # return true or false
print(String1.find('SEPTA')) # return index number
print("Well Done" if String1.find('hello world.') == True else "OPS!")
print(String2.find('Here', 10, 40)) # search in substring
print(String2.find('g', 10)) # search in substring

# 5- String Concatenation
print(f"{String1} {String2}")

newString1 = String1 + String2
print(newString1) # useing + Operator 

print("".join([String1, String2]))
newString2 = " ".join([String1, String2])
print(newString2) # useing join() method

print("% s % s" % (String1, String2)) # useing % Operator 

print("{} {}".format(String1, String2))
newString3 = "{} {}".format(String1, String2)
print(newString3) # useing format function

print(String1, String2) # useing ,

# 6- Commen built-in functions
String3 = " yOu   aRe   tHe   beSt "
print(String3.replace('   ',' ')) # replace a char with another, also useful for remove space
print(String3.lower())
print(String3.upper())
print(String3.startswith(' '))
print(String3.strip()) # earase white-space from start and end of a string

# 7- Rotate a string with generation function
def rotate(myStr):
    l = len(myStr)
    i = -1
    while(i >= -l):
        yield myStr[i]
        i -= 1

String4 = "hello world."
result = ''
for letter in rotate(String4):
    result = result + letter
print(String4,'\n The Rotate Is: \n', result)