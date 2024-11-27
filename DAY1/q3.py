#Write a program to extract the substring "Python" from "Welcome to Python Programming"

text = "Welcome to Python Programming"
start_index = text.find("Python")
substring = text[start_index:start_index + len("Python")]
print("Extracted substring:", substring)