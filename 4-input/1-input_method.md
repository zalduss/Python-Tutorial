
# input() Method 

## Introduction to input() Method
The `input()` method in Python is used to receive input from the user. This function allows your program to pause and wait for user input, which can be assigned to a variable for later use.

## How input() Works
- **Basic Usage**: 
  - Syntax: `variable = input(prompt)`
  - The `prompt` is a string that is displayed to the user. It's optional.
  - The function waits for the user to type something and press Enter.
  - The input received from the user **is always treated as a string**. (Important to remember when asking the user for numbers)

## Using input() to Get User Data

### Example 1: Asking for a Name
- **Code**:
  ```python
  name = input("Enter your name: ")
  print("Hello", name)
  ```
- **Explanation**:
  - The program prompts the user to enter their name.
  - The entered name is stored in the variable `name`.
  - The `print()` function then uses this variable to display a greeting.

### Example 2: Asking for Age
- **Code**:
  ```python
  age = input("Enter your age: ")
  print("You are", age, "years old.")
  ```
- **Explanation**:
  - The user's age is requested and stored as a string in the variable `age`.
  - The program then prints the age as part of a sentence.

## Converting Input to Other Data Types
Since `input()` returns a string, sometimes you need to convert this input into another data type, like an integer or float.

### Example: Converting to Integer
- **Code**:
  ```python
  age = input("Enter your age: ")
  age = int(age)
  print("Next year, you will be", age + 1, "years old.")
  ```
- **Explanation**:
  - The user's age is first stored as a string.
  - It's then converted to an integer using `int()`.
  - The program calculates and prints the user's age next year.

## Handling User Input
When using `input()`, it's important to handle unexpected or incorrect user input gracefully.

### Example: Basic Error Handling
- **Code**:
  ```python
  try:
      age = int(input("Enter your age: "))
      print("You entered:", age)
  except ValueError:
      print("Please enter a valid age (numbers only).")
  ```
- **Explanation**:
  - The `try` block attempts to convert the input to an integer.
  - If the conversion fails (e.g., the user enters a non-numeric value), the `except` block is executed.

## Challenge: Calculate a Dog's Age in Human Years
Create a Python script that:
- Asks the user for their dog's name and age.
- Calculates the dog's age in human years (1 dog year = 7 human years).
- Prints a message stating the dog's name and age in human years.

`"My dog, Louie, is 9 years old which equals 63 human years"`


