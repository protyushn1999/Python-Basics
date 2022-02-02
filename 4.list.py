'''Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous always which makes it the most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable.

List in Python are ordered and have a definite count. The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index. Each element in the list has its definite place in the list, which allows duplicating of elements in the list, with each element having its own distinct place and credibility.
Note- Lists are a useful tool for preserving a sequence of data and further iterating over it.'''



'''IMPORTANT - Difference between Methods and Functions is that Methods are bound to an object whereas Functions are not bound to an object.Functions operate on the data you pass to them as arguments. Methods are dependent on the class they belong to. They operate on the object that you pass to them.'''

name =['Python','C','C++','Java','PHP']
print(name)
name.sort() # dont return the sorted list, it changes the original list , writing [newlist = name.sort()] would return an error
print(name)
name.append('C#')
print(name)
name.insert(2,'Ruby') # insert at index 2 -> Ruby
print(name)
name.reverse()
print(name)
name.pop() # remove last element
print(name)
name.remove('Python') # remove element by value
print(name)

# multidimeansional Lists
languages = [['Python', 'C', 'C++', 'Java'], 
             ['PHP', 'Ruby', 'Javascript'],
             ['C#', 'Perl', 'Scala', 'Go']];
print(languages) # prints the languages list
print(languages[0][1]) # C
print(len(languages)) # prints the length of the list


# can store data of multiple data types
students = [['Protyush',23],
            ['Sourav',22],
            ['Rohit',21],
            ['Raj',20],
            ['Ravi',19]]
print(students)
print(type(students[0][1]))
print(type(students[2][0]))

newStudent = ['Rajesh',20]
students.append(newStudent)
print(students)

students[0][0] = 'Alia'
print(students)

'''append() method only works for the addition of elements at the end of the List, for the addition of elements at the desired position, insert() method is used. Unlike append() which takes only one argument, the insert() method requires two arguments(position, value). '''

newStudent1 = ['Tom',30]
students.insert(1,newStudent1)
print(students)

# lists slicing methods

friends =['Protyush','Tom','Ram','Rani','Vedant']
print(friends[0:2])


marks = [2,4,1,6,3,6]
totalmarks = sum(marks);
print(totalmarks)

'''***************************************'''


# Tuples


# A tuple is an immutable 
# (can’t change or modified) data type in Python.

a = ()              #It is an example of empty tuple
a = (1,)            #Tuple with only one element needs a comma
a = (1, 7, 2)       #Tuple with more than one element

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Protyush')
print(Tuple1)
print(len(Tuple1))
print(Tuple1[0]) # Access the first element of the Tuple


Tuple2 = ('Geeks', 'For', 'Geeks')
x,y,z = Tuple2
print(x)
print(y)
print(z)
