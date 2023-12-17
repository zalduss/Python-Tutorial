
# Python Functions Tutorial

## Introduction to Functions

In Python, functions are defined blocks of reusable code that perform a specific task. Functions help organize code, make it more readable, and allow for code reuse.

## Defining a Function

- **Syntax**:
  ```python
  def function_name(parameters):
      # code to execute
      return result
  ```

- **`def` Keyword**: Used to define a function.
- **Function Name**: A unique identifier to name the function.
- **Parameters**: Optional values that the function can accept to perform its task.
- **Return Statement**: Optionally returns a value back to the caller.

## Arguments
- An argument is a vlaue we pass into the function as its input when we call the function
- We use arguments to we can direct the function to do different kinds of work when we call it at different times

## Examples of Functions

### Example 1: Basic Function
- **Code**:
  ```python
  name = "John"
  greet(name)
  def greet(name):
    print(f"Hello, " + name + "!")
  
  ```
- **Explanation**:
  - `greet` is a function that returns the string "Hello, World!".
  - When `greet()` is called, it executes and prints "Hello, World!".

### Example 2: Function with Parameters
- **Code**:
  ```python
  def add(x, y):
      return x + y

  print(add(5, 3))
  ```
- **Explanation**:
  - `add` is a function that takes two parameters `x` and `y` and returns their sum.
  - `add(5, 3)` calls the function with 5 and 3, returning and printing 8.

### Example 3: Function with Default Parameters
- **Code**:
  ```python
  def greet(name="World"):
      return "Hello, " + name + "!"
  print(greet())
  print(greet("Alice"))
  ```
- **Explanation**:
  - `greet` has a default parameter `name` which defaults to "World".
  - Calling `greet()` without a parameter prints "Hello, World!".
  - Calling `greet("Alice")` prints "Hello, Alice!".

## Challenge: Creating and Using Functions

1. **Multiplication Function**: Write a function `multiply` that multiplies two numbers and returns the result. [Challenge 1](./challenge1.py)
2. **String Repeat Function**: Create a function `repeat_string` that takes a string and an integer and prints the string repeated that many times of the number. [Challenge 2](./challenge2.py)


