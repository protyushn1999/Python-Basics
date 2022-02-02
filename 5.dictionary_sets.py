# Dictionary is a collection of key-value pairs.  ==> Unordered Maps in C++

# Dictionary = {"Key1": "Value1", 
#               "Key2": "Value2"}

a = {"name" : "Protyush",
	"location" : "India",
	"marks" : [92,98,96]}

Dict = {
    1: "Python",
    2: "Java",
    3: "C++",
    4: "C#",
    5: "Perl",
    6: "Scala",
    7: "Go",
    8: "Javascript",
    "Type" : "Programming Language"
}


print(Dict[1]) # need to ensure that key must be present in dictionary else it will throw an error
print(Dict.get(1)) # returns the value of the key if present else returns None
print(Dict[2])
print(Dict["Type"])

# Creating a Nested Dictionary
# as shown in the below image
WelcomeMsg = {
                1: 'Geeks', 
                2: 'For',
                3:
                    {
                        'A' : 'Welcome', 
                        'B' : 'To', 
                        'C' : 'Geeks'
                    }
            }
 
print(WelcomeMsg)
print(WelcomeMsg.get(3))

# Pop() --> This method is used to return and delete the value of the key specified.
WelcomeMsg.pop(1)
print(WelcomeMsg)

# clear() --> All the items from a dictionary can be deleted at once.


'''****************************'''

# Sets

# Set is a collection of non-repetitive elements and it is unordered.

# The major advantage of using a set, as opposed to a list, 
# is that it has a highly optimized method for checking whether
#  a specific element is contained in the set.

'''Some points to remember about sets:
    Sets are unordered # Elements order doesn't matter
    Sets are unindexed # Cannot access elements by index
    There is no way to change items in sets
    Sets cannot contain duplicate values
'''

S = set()          # No repetition allowed!
S.add(1)
S.add(2)
print(S)
set = {1,2,3,4}
num = {2,3,4,5}
print(num)
print(set)

# Using update() method

# For addition of two or more elements Update() method is used. 
# The update() method accepts lists, strings, tuples as well as other sets as its arguments. In all of these cases, duplicate elements # are removed.

set.update([7,8,9,10])
print(set)

# Elements can be removed from the Set by using built-in remove() function
# but a KeyError arises if element doesn’t exist in the set. 
# To remove elements from a set without KeyError, use discard(), 
# if the element doesn’t exist in the set, it remains unchanged.

S.remove(1)
# S.remove(9) # shows keyerror if element doesn't exist
print(S)

S.discard(1) # if element doesn't exist, it remains unchanged and if presents, it is removed
print(S)

set.pop(); # removes an arbitrary element from the set and returns the element removed.
print(set)

# Union and Intersection of Sets

print(set.union({8,20}) ) # union of two sets
print(set.intersection({8,20}) ) # intersection of two sets
print(set.intersection({33,20}) ) # intersection of two sets if nothing is present, returns an empty set instead

