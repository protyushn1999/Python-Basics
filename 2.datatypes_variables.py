# Variable – Container to store a value
# Keywords – Reserved words in Python
# Identifiers – class/function/variable name
# Primarily there are five types of data types in python 
# Intgers, Floating point numbers, Strings, Booleans, None

a = "protyush"
b= 33
c = 66.44
d = True
e = None
# Print the variables
print(a,b,c,d,e);
print("The value of a is",a, "and the value of b is",b);

# Print the types of variables

print(type(a))
print(type(b))

# Typecasting  - Converting one data type to another

b = str(b)
print(type(b))
b = b + " new data type - got converted from integer to string"
print(b)

# taking input from the user

name = input("Enter Your Name");
print(name); 