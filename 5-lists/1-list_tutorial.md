
# Python List Basics

In Python, lists are a versatile data type that can hold a collection of items. Lists are similar to arrays in other languages, but in Python, they are known as `lists`. Let's explore the basics of Python lists.

![Python List](images/list.png)

To create a list in Python, we use square brackets and place the items we want to include in the list within them. The items can be of any type, and it's common to see lists containing numbers, strings, or even other lists.

Each item in a list is referred to as an `element`. Elements in a list are indexed, with the first element at index 0, the second at index 1, and so on. This zero-based indexing is standard across many programming languages.

Here's how we can create a list in Python:

```python
my_list = [374, 755, 398, 118, 289]
```

When we print a list, it displays all its elements:

```python
print(my_list)
```

#### List Constructor

Another way to create a list is by using the list constructor `list()`, though this is less common than using list literals.

```python
my_second_list = list((1, 2, 3, 4, 5))
```

Both methods create a list object in Python.

#### Accessing List Elements

You can access elements of a list by referring to the index number:

```python
my_list[0]
```

List elements can be used in expressions:

```python
my_list[0] + my_list[3]  # Sum of the first and fourth elements
```

Lists can contain different data types, including strings:

```python
fruits = ['apples', 'oranges', 'pears']
```

And even a mix of different types, or nested lists:

```python
mixed = [1, 'string', True, None, [1, 2, 3]]
```

#### List Length

The length of a list can be found using the `len()` function:

```python
print(len(my_list))  # 5
```

#### Modifying Lists

Lists are mutable, meaning their elements can be changed after the list is created. You can add, remove, or alter elements in a list.

To add an element to the end of a list:

```python
fruits.append('peaches')  # ['apples', 'oranges', 'pears', 'peaches']
```

To change an element:

```python
fruits[1] = 'mangos'
```

Adjusting the list size directly:

```python
fruits = fruits[:2]
```

Now, `fruits` will contain only the first two elements:

```python
['apples', 'oranges']
```


