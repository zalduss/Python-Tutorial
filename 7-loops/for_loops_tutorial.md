
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

**Step-by-Step Process:**

  1. **Initialization:** When the `for` loop starts, it initializes the loop variable `fruit` to the first element of the `fruits` list. Lists are indexed starting from 0, so the first element is at index 0.

2. **First Iteration (Index 0):** 
  - The loop variable `fruit` now holds the value `"apple"`, which is the item at index 0 of the list. 
  - The `print(fruit)` statement inside the loop is executed, printing `"apple"` to the console. 

3. **Second Iteration (Index 1):**

- After completing the first iteration, the loop moves to the next element in the list, which is `"banana"` at index 1.
- The loop variable fruit is updated to `"banana"`.
- The `print(fruit)` statement is executed again, this time printing `"banana"`.

4. **Third Iteration (Index 2):**

- The loop continues to the next (and last) element in the list, which is `"cherry"` at index 2.
- The loop variable `fruit` now contains `"cherry"`.
- The `print(fruit)` statement prints `"cherry"` to the console.

5. **End of Loop:**

- After the third iteration, there are no more elements left in the fruits list to iterate over.
- The `for` loop concludes its execution at this point.

### Example 2: Using the range() Function
- **Code**:
  ```python
  for i in range(5):
      print(i)
  ```
- **Explanation**:
  - This loop prints numbers from 0 to 4. The `range(5)` generates a sequence of numbers from 0 up to (but not including) 5.

1. **Initialization with range():** The `range(5)` function generates a sequence of numbers starting from 0 and ending at 4. It does not include the number 5, as the range in Python is up to, but not including, the end value.

2. **First Iteration (Start at 0):**

- The loop starts with the first number in the range, which is 0.
- The loop variable `i` is set to 0.
- The `print(i)` statement inside the loop is executed, printing 0 to the console.

3. **Second Iteration (Increment to 1):**

- The loop moves to the next number in the sequence, which is 1.
- The loop variable `i` is updated to 1.
- The `print(i)` statement prints `1`.

4. **Subsequent Iterations (Incrementing by 1):**

- The loop continues this process, incrementing i by 1 in each iteration.
- In each iteration, `i` takes the next value in the range (2, then 3, then 4).
- The `print(i)` statement prints each of these numbers in turn.

5. **End of Loop:**

- After reaching 4, the loop has no more numbers in the range to iterate over.
- The loop concludes its execution after printing `4`.

### Example 3: Looping Through a String
- **Code**:
  ```python
  for letter in "Python":
      print(letter)
  ```
- **Explanation**:
  - This loop prints each character in the string "Python".


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

Hint: Use the module operator (%). Review modules [if-conditions](../6-conditions/4-if_condition.md) and  [numbers](../3-variables/2-numbers.md)


**Expected Result:**

<details>
  <summary>Click For Solution</summary>


```Python
for i in range(11):
  if i % 2 == 0:
    print(i)
```

</details>

