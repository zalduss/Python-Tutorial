
# Python List Challenges

After covering some basic list operations, let's put your skills to the test with some simple challenges. Try to solve these using what you've learned so far. If you need to refer back to previous sections, that's perfectly okay.

**Note:** All challenges are based on topics we've already covered. For instance, I won't ask you to write a function if we haven't gone over functions yet. As a result, some early challenges might seem easy, especially if you have prior experience with Python.

### Challenge 1:

**Instructions:**

Mutate the following list using list methods we've discussed to achieve the expected result:

```python
my_list = [1, 2, 3, 4, 5]
```

**Expected Result:**

```python
print(my_list)
# [6, 5, 4, 3, 2, 1, 0]
```



<details>
  <summary>Click For Solution</summary>
  
  ```python
  my_list = [1, 2, 3, 4, 5]

  my_list.insert(0, 0)
  my_list.append(6)
  my_list.reverse()

  print(my_list) # [6, 5, 4, 3, 2, 1, 0]
  ```

</details>


### Challenge 2:

**Instructions:**

Merge `list1` and `list2` into a new list called `list3` with the following elements:

```python
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9, 10]
```

Note that both `list1` and `list2` include the number 5. You will need to find a way to eliminate the duplicate.

**Expected Result:**

```python
print(list3)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Hint**: Consider using list concatenation or the extend method, along with the remove method.

<details>
  <summary>Click For Solution</summary>
  
```python
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9, 10]

# Solution 1
list1.pop()
list3 = list1 + list2

print(list3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution 2
list3 = list1.copy()
list3.extend(list2[1:])

print(list3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

</details>


### Challenge 3:

**Instructions:**

Modify the following list to achieve the expected result:

```python
list1 = [1, 3, 5, 7, 9]
```

**Expected Result:**

```python
print(list1)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```



<details>
  <summary>Click For Solution</summary>
  
  ```python
  list1 = [1, 3, 5, 7, 9]

  list1.insert(0, 0)
  list1.insert(2, 2)
  list1.insert(4, 4)
  list1.insert(6, 6)
  list1.insert(8, 8)
  list1.append(10)
  list1.reverse()

  print(list1) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  ```

</details>