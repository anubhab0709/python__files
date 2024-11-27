#Write a python program to detect double spaces in a string and replace it with a single space.

text = input("Enter a string: ")
corrected_text = text.replace("  ", " ")
print("Corrected string:", corrected_text)