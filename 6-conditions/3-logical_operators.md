
# Python Logical Operators Tutorial

## Introduction to Logical Operators

Logical operators are used to combine conditional statements in Python. They are fundamental in making decisions and controlling the flow of execution in a program.

## Types of Logical Operators in Python

1. **AND (`and`)**: Returns True if both statements are true.
2. **OR (`or`)**: Returns True if one of the statements is true.
3. **NOT (`not`)**: Reverses the result, returns False if the result is true, and vice versa.

## Examples of Logical Operators

### Using AND
```python
x = 5
print(x > 3 and x < 10)  # True
print(x > 0 and x < 5)   # False
print(x == 5 and x < 6)  # True
```

### Using OR
```python
x = 5
print(x > 3 or x < 4)    # True
print(x < 5 or x == 5)   # True
print(x > 5 or x < 3)    # False
```

### Using NOT
```python
x = 5
print(not(x > 3 and x < 10))  # False
print(not(x < 5 or x > 6))    # True
print(not(x == 5))            # False
```

## Challenge: Determine True or False

Evaluate the following expressions and decide if they are True or False:

1. ```python
   print(4 > 3 and 2 < 5)   # True or False
   ``````

2. ````python
   print(1 == 2 or 3 == 3)  # True or False
   ```````
   
3. ````python
   print(not(4 != 4))       # True or False
   ```````

4. ````python
   print(7 > 8 and 5 < 6)   # True or False
   ```````

5. ````python
   print(3 <= 3 or 7 >= 8)  # True or False
   ```````

6. ````python
   print(not(0 == 0))       # True or False
   ```````

7. ````python
   print(6 > 5 and 4 < 3)   # True or False
   ```````

8. ````python
   print(2 == 2 or 2 != 2)  # True or False
   ```````

9. ```python
   print(not(5 > 6))        # True or False
   ```

10. ````python
    print(8 <= 8 and 9 > 10) # True or False
    ```````

Try to answer each question without running the code. Once you have your answers, run the script to check your understanding of logical operators.

Next