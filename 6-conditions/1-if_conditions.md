
# Python If Conditions Tutorial

## Introduction
In programming, conditional statements allow us to execute certain pieces of code depending on whether a specific condition is true or false. In Python, this is done using `if`, `elif`, and `else` statements. This tutorial will guide you through understanding and using these statements with practical examples.

## Understanding If Statements
- **What is an If Statement?**
  - An `if` statement is used to test a condition and execute a block of code if the condition is true.
  - Syntax: 
    ```python
    if condition:
        # code to execute if condition is true
    ```````

- **Simple Example**:
  - ```python
    if it_is_raining:
        print("Bring an umbrella.")
    ```````

## Adding Else
- **What is an Else Statement?**
  - `else` complements the `if` statement and is used to execute a block of code when the `if` condition is false.
  - Syntax: 
    ````python
    if condition:
        # code if condition is true
    else:
        # code if condition is false
    ``````

- **Real-World Example**:
  - ```python
    if it_is_raining:
        print("Bring an umbrella.")
    else:
        print("No need for an umbrella.")
    ```

## Introducing Elif
- **What is an Elif Statement?**
  - `elif` stands for 'else if' and is used to check multiple conditions after the initial `if`.
  - Syntax: 
    ```python
    if condition:
        # code if first condition is true
    elif another_condition:
        # code if another condition is true
    else:
        # code if no conditions are true
    ```````

- **Real-World Example**:
  - ```python
    if it_is_raining:
        print("Bring an umbrella.")
    elif it_is_sunny:
        print("Wear sunscreen.")
    else:
        print("Enjoy your day.")
    ```

## Nested If Statements
- **Using Nested Ifs**:
  - You can have `if` statements inside other `if` statements to check for further conditions.
  - Syntax: 
    ```python
    if condition:
        if another_condition:
            # code if both conditions are true
        else:
            # code if only the first condition is true
    else:
        # code if the first condition is false
    ```

## Example 

```python 
number = 5
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

```

## Challenges

### Challenge 1

Write a function called "check_age". 
- Given a person's name and age, "check_age" prints one of two messages: 
    - `"Go home, {insert_name_here}!"`, if they are younger than 21. 
    `"Welcome, {insert_name_here}!"`, if they are 21 or older. 
    
Write your solution inside [challenge1.py](./challenge1.py)


```python
def check_age(name, age):
    # your code here
```


### Challenge 2

Write a function called `greater_than_10`. 
- Given a number, `greater_than_10`, prints whether the given number is greater than 10. 
    - `greater_than_10(11) --> True`  
    - `greater_than_10(8) --> False`  
    
Write your solution inside [challenge2.py](./challenge2.py)


```python
def greater_than_10(num):
    # your code here
```


### Challenge 3

Write a function called `less_than_30`. 
- Given a number, `less_than_30`, prints whether the given number is less than 30. 
    - `less_than_30(15) --> True`  
    - `less_than_30(32) --> False`  
    
Write your solution inside [challenge3.py](./challenge3.py)


```python
def less_than_30(num):
    # your code here
```

### Challenge 4

Write a function called `equals_10`. 
- Given a number, `equals_10`, prints whether the given number is equal to 10. 
    - `equals_10(10) --> True`  
    - `equals_10(8) --> False`  
    
Write your solution inside [challenge4.py](./challenge4.py)


```python
def equals_10(num):
    # your code here
```

### Challenge 5

Write a function called `is_less_than`. 
- Given 2 numbers, `is_less_than`, prints whether num2 is less than num1. 
    - `is_less_than(9, 4) --> True`  
    - `is_less_than(6, 10) --> False`  
    
Write your solution inside [challenge5.py](./challenge5.py)


```python
def is_less_than(num1, num2):
    # your code here
```