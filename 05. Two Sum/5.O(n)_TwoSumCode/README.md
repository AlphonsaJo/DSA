# Two Sum

### Explanation 📝:

  - We iterate over nums once, so it's ```O(n)```.
  - For each number, we compute its complement ```(target - num)``` and check if it is in the dictionary.
  - If the complement exists, return the indices; otherwise, store the current number and its index in the dictionary.

### Concepts used 💡:

1. #### Dictionary (num_dict)
- A dictionary is a collection of ```key-value pairs```, where each key is unique, and it's associated with a value. 
- In your code, ```num_dict``` is used to store numbers ```(num)``` as keys and their corresponding indices ```(i)``` as values.
  
    Key Characteristics:
    - ```Lookup Time```: The average time complexity for lookups, inserts, and deletions in a dictionary is ```O(1)``` due to its hash table implementation.
    - ```Usage```: Here, ```num_dict``` allows for constant-time lookup to check if the complement (i.e., the number needed to reach the target sum) exists.
      
2. #### Enumerate() 

- The ```enumerate()``` function adds an index counter to an iterable (like a list) and returns an iterator that produces tuples of the form (index, element) on each iteration.

    Key Characteristics:
    - ```Simplifies Index Tracking```: Instead of manually managing an index variable with ```for i in range(len(nums))```, enumerate provides both the index ```(i)``` and the element ```(num)``` in a clean, concise way.
    - ```Usage```: In your code, ```enumerate(nums)``` allows you to iterate over both the index i and the corresponding number num in the list nums.

 ### How They Work Together in the Code 🛠️: 

  ```Dictionary (num_dict)```:
        It stores numbers as keys and their indices as values.
        Used to quickly look up if a number’s complement (target - current number) has been seen before.

  ```enumerate(nums)```:
        Provides both the index (i) and the number (num) in each iteration.
        This allows storing the index in num_dict and retrieving it when the complement is found.

Together, enumerate helps iterate over the list with index and value, while the dictionary provides a fast lookup mechanism for checking complements. This results in an efficient solution.

