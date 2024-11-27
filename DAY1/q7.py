#Write a program to count the number of vowels in a given string.

# Input string from the user
input_string = input("Enter a string: ")

# Initialize vowel count
vowel_count = 0

# Define the vowels
vowels = 'aeiouAEIOU'

# Loop through each character in the string
for char in input_string:
    if char in vowels:
        vowel_count += 1

# Output the result
print(f"The number of vowels in the string is: {vowel_count}")
