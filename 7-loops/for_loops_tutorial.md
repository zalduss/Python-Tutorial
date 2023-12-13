
# Python For Loops Tutorial

## Introduction to For Loops
In Python, a `for` loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string). It's a way to execute a block of code repeatedly for a certain number of times or over each item in a sequence.

## Understanding For Loops
- **Basic Syntax**:
  ```python
  for variable in sequence:
      # code to execute
  ```
- **Flow of Execution**:
  - The `variable` takes the value of the next element in the sequence on each iteration.
  - The loop continues until it has gone through all items in the sequence.

## Examples of For Loops

### Example 1: Iterating Over a List
- **Code**:
  ```python
  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(fruit)
  ```
- **Explanation**:
  - This loop prints each item in the `fruits` list.

### Example 2: Using the range() Function
- **Code**:
  ```python
  for i in range(5):
      print(i)
  ```
- **Explanation**:
  - This loop prints numbers from 0 to 4. The `range(5)` generates a sequence of numbers from 0 up to (but not including) 5.

### Example 3: Looping Through a String
- **Code**:
  ```python
  for letter in "Python":
      print(letter)
  ```
- **Explanation**:
  - This loop prints each character in the string "Python".

## Nested For Loops
- **Concept**:
  - A nested for loop is a loop inside another loop.
- **Example**:
  ```python
  for i in range(3):
      for j in range(2):
          print(f"i: {i}, j: {j}")
  ```
- **Use Case**:
  - Nested loops are often used for working with multi-dimensional data structures.

## Break and Continue in For Loops
- **Using `break`**: Exits the loop before it has gone through all items.
  ```python
  for number in range(10):
      if number == 5:
          break
      print(number)
  ```
- **Using `continue`**: Skips the current iteration and continues with the next one.
  ```python
  for number in range(10):
      if number == 5:
          continue
      print(number)
  ```

## Challenge: Practice with For Loops
Create a Python script to solve these tasks using for loops:

1. **Number Squares**:
   - Print the only even numbers from 0 to 10.

Hint: Use the module operator (%). Review modules [if-conditions](../6-conditions/1-if_conditions.md) and  [numbers](../3-variables/2-numbers.md)


**Expected Result:**

<details>
  <summary>Click For Solution</summary>


```Python
for i in range(11):
  if i % 2 == 0:
    print(i)
```

</details>

