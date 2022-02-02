# We can primarily write a string in three ways:

# Single quoted strings : a = 'Hello World'
# Double quoted strings : b = "Hello World"
# Triple quoted strings : c = '''Hello World'''
greeting = "Good Morning "
name  = 'Protyush'
print(name)
print(greeting)

# length of the string
print(len(name))

concatString = greeting + name
print(concatString)

'''In Python, individual characters of a String can be accessed by using the method of Indexing. Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on.While accessing an index out of the range will cause an IndexError. Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError. '''

print(name[0]) # prints the first character of the string
print(name[-1]) # -1 is the last character
print(name[-4]) # -4 is the 4th character from the end
print(name[2]) # 2 is the 3rd character

'''Updation or deletion of characters from a String is not allowed.Deletion of the entire String is done with built-in del keyword. This is because Strings are immutable. Only new strings can be reassigned to the same name. '''

# name[2] = "e" this doesn't work
# print(name)

# Slicing the string
print(name[0:4]) # prints the first 4 characters (includes the first index and excludes the last index)

print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:7]
print(name[-4:-1]) # is same as name[4:7]

# skip values that are not required
print(name[0: :2])
# length of the string
print(len(name))

# basic functions of strings

story = '''Python is a high-level, general-purpose and a very popular programming language. Python programming language is being used in web development, Machine Learning applications, along with all cutting edge technology in Software Industry. Python Programming Language is very well suited for Beginners, also for experienced programmers with other programming languages like C++ and Java.'''

storyLength = len(story)
storyEndsWith = story.endswith('Programming Language') 
storyCountH = story.count('h')
storyCountIs = story.count('is')
storyFindPython = story.find('Python')
storyReplacePython = story.replace("Python", "Python3")

print(storyLength)
print(storyEndsWith)
print(storyCountH, storyCountIs)
print(storyReplacePython)

# ToDo --> string.format()

'''String.index	--> Returns the position of the first occurrence of substring in a string
String.isdigit() --> Returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
String.isalpha() --> Returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.
string.isdecimal() --> Returns true if all characters in a string are decimal.
'''