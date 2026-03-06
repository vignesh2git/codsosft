# Rock-Paper-Scissors Game Application

import random

def play_rps():
    print("===== 🎮 Welcome to Rock-Paper-Scissors Game! =====")

    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]


    while True:
        print("\nChoose your move: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in options:
            print("Invalid choice. Please select rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("You lose this round! 😢")
            computer_score += 1

        # Show current scores
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        # Ask if user wants to play again
        again = input("\nDo you want to play another round? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! Final Score -> You: {} | Computer: {}".format(user_score, computer_score))
            break

if __name__ == "__main__":
    play_rps()
