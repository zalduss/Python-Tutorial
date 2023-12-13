
# Python List Modification Methods Tutorial

## Introduction to Modifying Lists
Python lists are dynamic and can be modified in various ways. This doc covers common methods to modify lists.

## List Modification Methods

### Adding Elements
- **append()**: Adds an element to the end of the list.
  ```python
  fruits = ['apple', 'banana']
  fruits.append('cherry')
  ```

- **insert()**: Inserts an element at a specified index.
  ```python
  fruits.insert(1, 'orange')
  ```

- **extend()**: Adds elements of a list (or any iterable) to the end of the current list.
  ```python
  fruits.extend(['grape', 'melon'])
  ```

### Removing Elements
- **remove()**: Removes the first occurrence of a specified element.
  ```python
  fruits.remove('banana')
  ```

- **pop()**: Removes the element at a specified index (default is the last item).
  ```python
  last_fruit = fruits.pop()
  ```

- **clear()**: Removes all elements from the list.
  ```python
  fruits.clear()
  ```

### Other Modifications
- **reverse()**: Reverses the order of the list elements.
  ```python
  fruits.reverse()
  ```

- **sort()**: Sorts the elements of the list.
  ```python
  numbers = [3, 1, 4, 1, 5, 9, 2]
  numbers.sort()
  ```

- **copy()**: Creates a shallow copy of the list.
  ```python
  fruits_copy = fruits.copy()
  ```

- **count()**: Returns the number of elements with the specified value.
  ```python
  count_ones = numbers.count(1)
  ```

- **index()**: Returns the index of the first element with the specified value.
  ```python
  index_of_cherry = fruits.index('cherry')
  ```

### Modifying Lists with Operators
- **Concatenation (`+`)**: Combines two lists.
  ```python
  combined_fruits = fruits + ['pear', 'peach']
  ```

- **Repetition (`*`)**: Repeats the list a specified number of times.
  ```python
  repeated_numbers = numbers * 2
  ```




