import string


# Take the input
x = input("Enter a sentence. ")

# Use the join and split methods to print words backwards
new_text = ' '.join(x.split(' ')[::-1])

# Print the output
print(new_text)