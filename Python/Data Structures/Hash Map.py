#! Hash table in python
#!  hash map, also known as key value pairs, not same as hash table
#! uses a dictionary then assign each key(like the id) to a value(value of the key)
#! keys must be unique, values can be the same

# ! EX 1 creating and adding values
# Creating an empty hash map (dictionary)
hash_table = {}

# Adding key-value pairs
hash_table['apple'] = 1
hash_table['banana'] = 2
hash_table['orange'] = 3

print(hash_table)  # Output: {'apple': 1, 'banana': 2, 'orange': 3}

#! getting values
# Access a value by key
print(hash_table['apple'])  # Output: 1

# Using `get()` to avoid KeyError if key is not present
print(hash_table.get('banana'))  # Output: 2
print(hash_table.get('grape', 'Not found'))  # Output: Not found

#! modifing values
# Modify the value for a key
hash_table['apple'] = 10
print(hash_table)  # Output: {'apple': 10, 'banana': 2, 'orange': 3}

#! deleting values
# Using `del` to remove a key-value pair
del hash_table['banana']
print(hash_table)  # Output: {'apple': 10, 'orange': 3}

# Using `pop()` to remove a key and return its value
value = hash_table.pop('orange')
print(value)  # Output: 3
print(hash_table)  # Output: {'apple': 10}

#! Iteration
# Iterating over keys
for key in hash_table:
    print(key, hash_table[key])

# Iterating over key-value pairs
for key, value in hash_table.items():
    print(f'{key}: {value}')

#! checking for keys in dic
# Check if a key exists in the dictionary
if 'apple' in hash_table:
    print("Apple is in the hash table")
    
# ! adding key values to hash table using a list 
counter = {}

# List of items to count
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Loop through each item
for item in items:
    # Initialize the key if it doesn't exist, setting the starting count to 0
    if item not in counter:
        counter[item] = 0 # this adds the key of the item to the hash table and sets the value to 0
    
    # Increment the count for this item by 1 as it appears in the list
    counter[item] += 1 # this adds 1 to the value of the key which already exists, if it dosent it will add it like above (but we check first that it exists)

print(counter)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

#  ! EX with str
# Sample string
text = "hello world"

# Initialize an empty dictionary for counting
letter_count = {}

# Loop through each character in the string
for letter in text:
    # Skip spaces (or any other characters you don't want to count)
    if letter == " ":
        continue

    # Check if the letter is already a key in the dictionary
    if letter not in letter_count:
        letter_count[letter] = 0  # Initialize it if it doesn't exist

    # Increment the count for this letter
    letter_count[letter] += 1

print(letter_count)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# ! EX (just keys no values) finding vowels in a string array
# Creating a hash table to store vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
vowelscounter = 0
# Iterating over each character in the string
for char in 'hello':
    # Checking if the character is a vowel
    if char in vowels:
        vowelscounter += 1
        
print("number of vowels: ",vowelscounter)

# ! EX (with key and value) finding values of gems given a array of gem strings
# Creating a hash table to store gem values
gem_values = {'ruby': 10, 'emerald': 20, 'sapphire': 30, 'topaz': 40, 'diamond': 50}
earning = 0
# Iterating over each gem in the array
for gem in ['ruby', 'emerald', 'diamond', "dirt"]:
    # Checking if the gem exists in the hash table
    if gem in gem_values:
        earning += gem_values[gem]
        print(f'{gem}: {gem_values[gem]}') # prints the type (gem) and value of the gem (genvalue[gem])

print(earning) # prints the total earning from the gems

# using pythons get() funcrtion to safly get the value of a key from a dictionary without throwing an error if the key is not found
# usally we say x = map[value]  but what is value DNE, use get() to get its value and then we can modify map[value] knowing it exists
# EX;
map = {'a': 1, 'b': 2, 'c': 3}
print(map.get('a')) # prints 1
print(map.get('d')) # prints None

# For sorting dictionaries by keys or values, you can use the sorted() function in combination with the dict() function to convert the soted obj to a dictionary
# sort by key
my_dict = {'b': 2, 'a': 3, 'c': 1}
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)  # Output: {'a': 3, 'b': 2, 'c': 1}
# sort by value
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# filter EX, filter out eeryh=thing except the keys that are greater than 1
filterd_by_keys= {'b': 2, 'a': 3, 'c': 1}
filterd_by_keys = dict(filter(lambda item: item[1] > 1, filterd_by_keys.items()))
print(filterd_by_keys)

## !! HASH MAP VS HASH TABLE
"""
Comparison Between Python's `dict` (HashMap) and Thread-Safe Dictionary (Hashtable):

1. Thread Safety:
   - Python dict (HashMap): Not thread-safe.
   - Thread-safe dict (Hashtable): Thread-safe with locks.

2. Null Keys/Values:
   - Python dict (HashMap): Supports None as keys/values.
   - Thread-safe dict (Hashtable): Supports None with proper handling.

3. Performance:
   - Python dict (HashMap): High for single-threaded apps.
   - Thread-safe dict (Hashtable): Slower due to synchronization.

4. Built-in Support:
   - Python dict (HashMap): Yes, built-in (dict).
   - Thread-safe dict (Hashtable): No, requires manual implementation.
"""

from threading import Lock

class ThreadSafeDict:
    def __init__(self):
        self.dict = {}
        self.lock = Lock()

    def set(self, key, value):
        with self.lock:
            self.dict[key] = value

    def get(self, key):
        with self.lock:
            return self.dict.get(key)

# Usage
ts_dict = ThreadSafeDict()
ts_dict.set("key1", "value1")
print(ts_dict.get("key1"))  # Output: value1
