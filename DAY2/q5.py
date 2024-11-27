# Given a list of names: ['Alice' 'Bob' 'Charlie' 'Diana'], write a program that usesenumerate to print each name along 
# with its position in the list.Also start the index from 1 instead of 0.

names = ['Alice', 'Bob', 'Charlie', 'Diana']
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")