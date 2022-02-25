# Strings
s1 = "America"
s2 = "Japan"

# First Letters
first_letters = s1[0] + s2 [0]

# Middle Letters
s1_length = int(len(s1)) / 2
s2_length = int(len(s2)) / 2

middle_letters = s1[int(s1_length)] + s2[int(s2_length)]

# Last Letters
last_letters = s1[-1] + s2[-1]

# Print Output
print(first_letters + middle_letters + last_letters)