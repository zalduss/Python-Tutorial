
# Understanding Scope in Python

## Introduction to Scope

Scope in programming refers to the region of the program where a defined variable can be accessed and manipulated. In Python, scope is determined by the location where a variable is declared and plays a crucial role in variable visibility and lifespan.

## Types of Scopes in Python

1. **Local Scope**: Variables defined within a function belong to the local scope of that function, and can only be used inside that function.
2. **Global Scope**: Variables that are defined at the top level of a script or program have a global scope, and are visible throughout the program unless shadowed by a locally scoped variable.

To help us understand this conept lets use it in a real life analogy.

### Household Analogy (Local and Global Scope)
* **Local Scope:** Imagine you have a room in your house where you keep personal belongings that only you use (such as your bedroom or personal bathroom). These items are like variables in a function's local scope; they are only accessible within that function (or room).
* **Global Scope:** The living room, however, is a common space where items are accessible to everyone in the house. This is like a global scope in programming, where variables are accessible from anywhere in the program.

## Examples of Scope

### Example 1: Local Scope
```python
def my_room():
    item = "toothbrush"  # Local variable
    print(item)

my_room()
# Trying to print local_var outside the function will result in an error.
```

### Example 2: Global Scope
```python
item = "TV Remote"  # Global variable

def living_room():
    print(item)  # Accessing a global variable inside a function

my_function()
print(item)  # Accessing the global variable outside the function
```

