#Write a python program to create a rock-paper-scissors game in Python against the computer.

import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main function for the game
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'exit' to quit the game.\n")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result, "\n")

# Start the game
rock_paper_scissors()