# Python Sets 📦
- A set in Python is an unordered collection of unique elements.
- Sets are mutable, meaning you can add or remove items, but they do not allow duplicates. 
- They are commonly used for membership testing (to check whether a member exists or not), eliminating duplicates, and set operations like union, intersection, difference, and symmetric difference.

### Creating a Set
``` python
# Creating a set
my_set = {1, 2, 3, 4}

# Using the set() function
another_set = set([1, 2, 3, 4])
```

### Summary of Operations
| Operation                | Description                                      |
|--------------------------|--------------------------------------------------|
| `add()`                  | Adds an element to the set.                      |
| `remove()`               | Removes an element from the set.                 |
| `discard()`              | Removes an element without raising an error.     |
| `union()`                | Returns the union of sets.                       |
| `intersection()`         | Returns the intersection of sets.                |
| `difference()`           | Returns the difference of sets.                  |
| `symmetric_difference()`  | Returns elements in either set, but not both.       |



### 1. **Adding Elements**
You can add elements to a set using the `add()` method.

```python
my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
print(my_set)  # Output: {1, 2, 3, 4}
```

### 2. **Removing Elements**
You can remove elements using the `remove()` or `discard()` methods.

```python
my_set = {1, 2, 3}
my_set.remove(2)  # Removes element 2
print(my_set)  # Output: {1, 3}

my_set.discard(3)  # Removes element 3
print(my_set)  # Output: {1}
```

### 3. **Union**
Combines elements from both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

### 4. **Intersection**
Returns elements common to both sets.

```python
intersection_set = set1.intersection(set2)  # {3}
print(intersection_set)  # Output: {3}
```

### 5. **Difference**
Returns elements in the first set but not in the second.

```python
difference_set = set1.difference(set2)  # {1, 2}
print(difference_set)  # Output: {1, 2}
```

### 6. **Symmetric Difference**
Returns elements in either set, but not both.

```python
sym_diff_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
print(sym_diff_set)  # Output: {1, 2, 4, 5}
```

