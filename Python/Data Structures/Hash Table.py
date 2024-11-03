#! Hash table in python
#! not the same as hash map, also known as key value pairs
#! IDEA: create a dictionary then assign each key(like the id) to a value(value of the key)

# ! EX 1 creating and adding values
# Creating an empty hash table (dictionary)
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