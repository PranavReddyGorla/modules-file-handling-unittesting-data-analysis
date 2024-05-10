text = "Hello World"

# Create an empty dictionary to store character counts
char_count = {}

# Iterate through each character in the string
for char in text:
    # Check if the character is already in the dictionary
    if char in char_count:
        # If it is, increment its count by 1
        char_count[char] += 1
    else:
        # If it's not, add it to the dictionary with a count of 1
        char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}': {count}")
