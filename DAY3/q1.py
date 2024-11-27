#Write a Python program to create a dictionary of Hindi words with their English translations. Extend the program to allow 
# the user to look up the English translation of a Hindi word.

english_to_bengali = {
    "hello": "হ্যালো",
    "book": "বই",
    "water": "জল",
    "sky": "আকাশ",
    "love": "ভালবাসা"
}

print("English to Bengali Dictionary")
print("Enter exit to exit the program")

while True:
    word1 = input("\nEnter a Word: ")
    word2 = word1.lower()
    if word2 == "exit":
        break
    if word2 in english_to_bengali:
        print(f"{word1} means {english_to_bengali[word2]} in Bengali")
    else:
        print("Word not found in Dictionary")
