# We can primarily write a string in three ways:

# Single quoted strings : a = 'Hello World'
# Double quoted strings : b = "Hello World"
# Triple quoted strings : c = '''Hello World'''
greeting = "Good Morning "
name  = 'Protyush'
print(name)
print(greeting)

concatString = greeting + name
print(concatString)

print(name[0]) # prints the first character of the string
print(name[-1]) # -1 is the last character
print(name[-4]) # -4 is the 4th character from the end
print(name[2]) # 2 is the 3rd character

# name[2] = "e" this doesn't work
# print(name)

# Slicing the string
print(name[0:4]) # prints the first 4 characters (includes the first index and excludes the last index)

print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:7]

# length of the string
print(len(name))