'''A function is a group of statements performing a specific task.
When a program gets bigger in size and its complexity grows, 
it gets difficult for a programmer to keep track of which piece of code is doing what!
A function can be reused by the programmer in a given program any number of times.
Functions can be both built-in or user-defined. 
It helps the program to be concise, non-repetitive, and organized.'''


# Syntax 
# def function_name(parameters):
#     """docstring"""
#     statement(s)
#     return expression
a = 20
b = 30

def add(a,b):
    sum = a + b
    print(sum)

add(a,b)


def sum(a = 2, b = 3):
    sum = a+b
    print(sum)
    return sum

res = sum(4,5) # It can override the default values
print(res)

def greet():
    pass # pass is a keyword in python which does nothing ==> it is used to create empty functions


# global keyword and local variables

def f():
    s = 'I am inside f'
    print(s)
s = 'I am outside f'
print(s)
f()

def g():
    p = 'I am inside g'
    print(p)

g() 
# print(p) # throws an error as p is not defined in the global context


# This function uses global variable s
def h():
    print("Inside Function", q)
# Global scope
q = "I love myself"
h()
print("Outside Function", q)


# This function uses global variable s
def f():
    ''' s += 'GFG' # This is a local variable and cant access the global variable s
    print("Inside Function", s) '''
 
# Global scope
s = "I love Geeksforgeeks"
f()



# hence to access the global variable inside  the function to modify it we use the keyword global variable

def fun():
    global line
    line  = line + " which is accessed inside the function"  # it directly accesses the global variable and changes it
    print(line)

line = 'this a line globally'
print(line)
fun()
print(line)



'''In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
1.)*args (Non-Keyword Arguments)
2.)**kwargs (Keyword Arguments)
'''

'''
*args* is a keyword argument
It is used to pass a non-keyworded variable number of arguments to a function.
'''
def myFun(*argv):
    for arg in argv:
        print (arg)

list = []

while True:
    userInput = input('Please enter your words to be typed : ')
    if userInput == 'quit':
        break
    else:
        list.append(userInput)

myFun(list)


'''The special syntax **kwargs in function definitions in python
 is used to pass a keyworded, variable-length argument list.
 We use the name kwargs with the double star. 
 The reason is because the double star allows us to pass 
 through keyword arguments (and any number of them).
 '''

def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun(first ='Hello', mid ='Mr', last='Protyush')   