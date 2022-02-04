'''
Class ==> A class is a blueprint for creating objects.
Object ==> An object is an instantiation of a class.
           When class is defined, a template(info) is defined.
           Memory is allocated only after object instantiation.
'''

# Class have attributes and methods to define the class
# Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. 
# A class is like a blueprint for an object.


'''
Defination/ Syntax

class ClassName:
    # Statement 1
    .
    .
    .
    # Statement n
'''

class Animal:

    def fun(self):
        # print(self)
        print(self.name)
        print(self.age)
        print(self.color)

Dog = Animal()
Dog.name = 'Tommy'
Dog.age = 18
Dog.color = 'Black'

print(Dog.name)
Dog.fun();


class Employee:
    company = "Nutanix"
    
    def printDetails(self):
        print("Company Name: ", self.company)
        print("Employee Name: ", self.name)
        print("Employee Age: ", self.age)
        print("Employee Salary: ", self.salary)
        print("Employee Experience: ", self.experience)

    def getSalary(self):
        return self.salary


protyush = Employee()
print(protyush.company)
protyush.name = "Protyush Nayak"
protyush.age = 18
protyush.salary = 100000
protyush.experience = 4
protyush.printDetails()


salaryProtyush = protyush.getSalary()
print(salaryProtyush)
# this line in Python gets converted to 
# salaryProtyush = Employee.gelSalary(protyush)

salaryprotyush = Employee.getSalary(protyush)
print(salaryprotyush) # 100000 same ans as above


'''Class methods must have an extra first parameter in the method definition.
 We do not give a value for this parameter when we call the method, Python provides it.
If we have a method that takes no arguments, then we still have to have one argument.'''


# Constructors in Python - It helps to create a object by justing passing the values
# Syntax 
'''
def __init__(self, atrr1, attr2, attr3, attr4):
    self.attr1 = attr1
    self.attr2 = attr2
    self.attr3 = attr3
    self.attr4 = attr4
'''

class Student:
    def __init__(self,name,rollNo,section,age,house):
        self.name = name
        self.rollNo = rollNo
        self.section = section
        self.age = age
        self.house = house

    def printDetails(self):
        print("Student Name: ", self.name)
        print("Student Roll No: ", self.rollNo)
        print("Student Section: ", self.section)
        print("Student Age: ", self.age)
        print("Student House: ", self.house)

    def getHouse(self):
        return self.house
    def setHouse(self,house):
        self.house = house

    def getAge(self):
        return self.age
    def setAge(self,age):
        self.age = age


student1 = Student("Protyush", 31, "A", 18, "Gryffindor")
student2 = Student("Raj", 32, "B", 19, "Slytherin")
student3 = Student("Rajesh", 33, "C", 20, "Hufflepuff")
student4 = Student("Preetam", 34, "D", 21, "Ravenclaw")

student1.printDetails()
student2.printDetails()

student3.setHouse("Gryffindor")
student4.setAge(22)

student3.printDetails()
student4.printDetails()


# Instance variables are for data, 
# unique to each instance and class variables are for attributes 
# and methods shared by all instances of the class.

#  Instance variables are variables whose value 
# is assigned inside a constructor or method with self whereas
#  class variables are variables whose value is assigned in the class.

class Dog:

    animal = 'Dog'  # Class variable

    def __init__(self, breed, color):
        self.breed = breed  # Instance variable
        self.color = color  # Instance variable
    
    def printDetails(self):
        print("Breed: ", self.breed)
        print("Color: ", self.color)
        print("Animal: ", self.animal)

tommy = Dog('Lab', 'Black')
tommy.printDetails()
charlie = Dog('German Shepherd', 'White')
charlie.printDetails()

#  Class variables can be accessed using class name also
print(Dog.animal)
# Class variables can obviously be accessed using object name also just like other instance variables
print(tommy.animal)


# Static Methods - Static methods are methods that are called without passing the object as an argument.

'''
class ClassName:
    def __init__(self, attr1):
        self.attr1 = attr1
    
    def printDetails(self):
        print("Class Name: ", self.attr1)
    
    @staticmethod
    def greetUser():
        print("Hello User")
'''


'''********************* Inheritance **********************'''

# Inheritance is a way of creating a new class from an existing class.
# Base class is the class from which the new class is derived.
# Derived/Child class is the class which inherits the base class.

# Syntax
'''
class Employee:
     # Class statement
     # This is the Base Class


class Programmer(Employee):
    # Class statement
    # This is the Derived Class
    # It can use all the methods and attributes of the Base Class
    # It can overwrite and and new attributes and methods in the Programmer Class
'''

# Single, Multiple, Multilevel and Heicharchical Inheritance

# Single Inheritance

# Base class or Parent class
class Child:

	# Constructor
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def isStudent(self):
		return False

# Derived class or Child class
class Student(Child):

	def isStudent(self):    # Changing the method isStudent() to return true value
		return True

std = Child("Protyush")
print(std.getName(), std.isStudent())
std = Student("Aakanksha")
print(std.getName(), std.isStudent())


# Multiple Inheritance

# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)

# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)


s1 = Son()
s1.parents()
# changing the name of the father and mother
s1.fathername = "Saroj"
s1.mothername = "Jayanti"
s1.parents()

