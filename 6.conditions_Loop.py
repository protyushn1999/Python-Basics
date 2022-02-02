# Conditions Statement
# if elif else statement is used to indicate that a condition must be true in order for the code to be executed.

# Syntax Statements
# if (condition_name):
#     code to be executed if condition is true
# elif (condition_name):
#     code to be executed if condition is true
#  else:
#     code to be executed if condition is false


# python program to illustrate If statement

i = 10

if (i > 15):
	print("10 is less than 15")
print("I am Not in if")


j = 20

if(j > 25):
    print("j is greater than 25")
elif(j > 22):
    print("j is greater than 22")
elif(j > 10):
    print("j is greater than 10")
else:
    print("j is less than 10")



# nested conditionals statements

age = input("Enter your age: ")
age = int(age)

print('Your age is: ', age) 

if(age > 18):
    print("You are eligible to vote")
    if(age > 21):
        print("You are eligible to drink")
    else:
        print("You are not eligible to drink")
else:
    print("You are not eligible to vote")
    if(age < 16):
        print("You are eligible to play video games")
    else:
        print("You are not eligible to play video games")

# Chaining Opeartors with if statements

# need to find if a < b < 
# gen syntax in other programming languages ==> a < b && b < 
# in python , just write a < b < c to evaluate



'''***********************************'''

# loops are used to execute a block of code repeatedly
# two loops - while and for loops

num = 0;
while num < 10:
    print("Hello", num)
    num = num + 1

fruits  = ['Banana', 'Apple', 'Mango', 'Orange', 'Pineapple', 'Strawberry', 'Guava', 'Papaya']
length  = 0
while length < len(fruits):
    print(fruits[length])
    length = length + 1

# for loop - for loop is used to iterate through a sequence like a list, tuple, or string (iterables)

i = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096]

for num in i:
    print(num)
