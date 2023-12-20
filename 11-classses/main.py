# Class
class MyClass:
    # Constructor
    # What ia a constructor?
    # What does self mean? 
    # What does __init__ mean?
    def __init__(self, nums):
        # Member vairable
        # What is self
        # What is member vairable
        # Where is nums coming from
        # Where is self.nums coming from
        self.nums = nums
        self.size = len(nums)

    # Member function
    # What is a member function
    # What is self
    # Why is self a required parameter --> Give us access to our member variables defined above
    # self key word is required as a param
    def get_length(self):
        return self.size
    
    def get_double_length(self):
        # Why is nothing passed into the function when clearer shown above it has self as a parameter
        return 2 * self.get_length()

"""
A constructor in Python is a special method for creating and initializing an object created within a class. The constructor method is defined within the class and is named init.

When you create an object of the class, Python automatically calls the init method of the class to initialize the object. The arguments of the init method are used to pass the values for the object attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name) # Output: John
print(p1.age)   # Output: 36

In this example, the __init__ method takes two parameters, name and age, which are used to initialize the name and age attributes of the Person objects. When you create a Person object like p1, Python automatically calls the __init__ method with the specified arguments.
"""


"""
does the name have to be init?

No, the name of the initializer method in Python does not have to be init. In fact, the recommended practice is to name the initializer method based on the class name itself.

Here's an example:

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_employee(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

In this example, the initializer method is named __init__. However, if you prefer, you can name it Employee as shown below:

class Employee:
    def Employee(self, name, age):
        self.name = name
        self.age = age

    def display_employee(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

In this revised example, the initializer method is named Employee instead of __init__.

It's worth noting that while it's technically possible to name the initializer method something other than __init__, doing so is not idiomatic and can lead to confusion for other developers. It's generally best to stick with the standard naming convention for initializer methods in Python.
"""