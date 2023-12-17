
# Python Variables and Data Types Tutorial

## Introduction
In programming, variables are used to store data that can be used and manipulated throughout a program. Python, being a dynamically-typed language, does not require explicit declaration of the data type of a variable. The data type is inferred at runtime based on the value assigned to the variable.

## Understanding Variables
- **What is a Variable?**
  - A variable is like a container in programming that holds data. It can be thought of as a label you can assign to a value.
  - Variables allow you to store, modify, and reuse data throughout your program.

- **Declaring and Using Variables**
  - In Python, you declare a variable by typing a name and assigning it a value using the `=` operator.
  - Example: `my_variable = 10`

- **Variable Naming Rules**
  - Must start with a letter or underscore.
  - Can only contain letters, numbers, and underscores.
  - Are case-sensitive (`myVariable`, `MyVariable`, and `MYVARIABLE` are different variables).

## Data Types in Python
Python supports various data types, but here we'll focus on the most commonly used ones:

- **Integers**: Whole numbers without a decimal point.
  - Example: `age = 25`
- **Floats**: Numbers with a decimal point.
  - Example: `height = 5.9`
- **Strings**: Sequence of characters, enclosed in single or double quotes.
  - Example: `name = "John"`
- **Booleans**: Represents `True` or `False`.
  - Example: `is_student = True`

## Working with Variables
- **Reassigning Variables**
  - You can change the value of a variable by reassigning it.
  - Example: `age = 30`
- **Dynamic Typing**
  - Python allows changing the data type of a variable in the program.
  - Example: `my_var = 10` (integer) and later `my_var = "ten"` (string).

## Operations on Variables
- **Arithmetic Operations**: Can be used with numerical data types (integers and floats).
  - Examples: `+`, `-`, `*`, `/`
- **Concatenation**: Joining of strings.
  - Example: `full_name = "John" + " " + "Doe"`

In programming, numbers are a fundamental data type used in various operations and calculations. There are typically two main types of numbers used in programming:

**Integers**: Whole numbers without a fractional component.
**Floats**: Numbers that include a fractional part, commonly represented with a decimal point.
<br>

```Python
# Declaring different types of numbers
integer = 4 # An integer value
float = 4.7 # A floating-point number


# Some operations with numbers
sum = 4 + 5 # Adding two numbers
difference = 9 - 4 # Subtracting two numbers
product = 4 * 5 # Multiplying two numbers
quotient = 20 / 4 # Dividing two numbers
remainder = 11 % 5 # Moduling two numbers
```

### The Modulo Operator
- Modulo Operator (%): This operator is used to find the remainder after division of one number by another.
- Commonly used to determine if a number is even or odd.

add more


## Challenge
**Instructions**:

Input two numbers into two seperate variables. Add these varriables and together and store the answer into the variable `sum`. Then print the sum to the terminal.


**Expected Result:**

<details>
  <summary>Click For Solution</summary>
  
  Here is one possible solution

```Python
num1 = 10
num2 = 20

sum = num1 + num2
print(sum) # prints 30
```


## Challenge: Practice with Variables and Data Types
Now that you've learned about variables and data types, it's time to put your knowledge into practice.

**Objective**: Create a Python script that accomplishes the following tasks:
1. Create a variable named `item_price` and assign it a float value.
2. Create a variable named `quantity` and assign it an integer.
3. Calculate the total cost and store it in a variable named `total_cost`.
4. Print a message to the console that shows the item price, quantity, and total cost in a readable format.

**Example Output**:

- If `item_price` is 5.99 and `quantity` is 3, your program should print:
  - "Item price: $5.99, Quantity: 3, Total cost: $17.97"

- Write the solution in `cost_of_goods.py`
