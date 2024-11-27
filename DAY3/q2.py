#Design a Python program that runs a quiz game similar to "Kaun Banega Crorepati (KBC).
# " Use a list of dictionaries to store each question along with four options, the correct answer, and a prize for each question. 
# Display the total prize money won at the end.

prize = 10000

questions = ["Who is the Prime Minister of India?",
             "Capital of India?",
             "Who is the President of India?",
             "Who is the Chief Minister of West Bengal?",
             "Captain of Indian Cricket Team?",]


options =[
    {"A" : "Narendra Modi",
    "B" : "Rahul Gandhi",
    "C" : "Amit Shah",
    "D" : "Yogi Adityanath",
    "ans" : "A"},
    
    {"A" : "Mumbai",
    "B" : "Gujarat",
    "C" : "New Delhi",
    "D" : "Kolkata",
    "ans" : "C"},
    
    {"A" : "Dropadi Murmu",
    "B" : "Ramnath Kovind",
    "C" : "Pranab Mukherjee",
    "D" : "Narendra Modi",
    "ans" : "A"},
    
    {"A" : "Virat Kohli",
    "B" : "Hardik Pandya",
    "C" : "Rohit Sharma",
    "D" : "Jasprit Bumrah",
    "ans" : "C"},
]


for i in range(len(questions)):
    print(f"\nQuestion", i+1, ":", questions[i])
    for j in ["A", "B", "C", "D"]:
        print(j, ":", options[i][j])
    ans = input("Enter your answer: ")
    ans = ans.upper()
    if ans == options[i]["ans"]:
        print("\nCorrect Answer!" + "\nYou have won Rs.", prize)
        prize = prize * 10
    else:
        print("Wrong Answer!")
        break