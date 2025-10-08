# Program to remove punctuations from a given string

# Define punctuation characters
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Take input from the user
input_str = input("Enter a string: ")

# Remove punctuations
no_punct = ""
for char in input_str:
    if char not in punctuations:
        no_punct += char

# Display the result
print("\nString without punctuations:")
print(no_punct)
