import random

user_score = 0
computer_score = 0

print("Rock Paper Scissors Game")

while True:
    print("\nChoose one option:")
    print("rock")
    print("paper")
    print("scissors")

    user = input("Enter your choice: ").lower().strip()
    computer = random.choice(["rock", "paper", "scissors"])

    print("You selected:", user)
    print("Computer selected:", computer)

    if user == computer:
        print("Result: Tie")
    elif user == "rock":
        if computer == "scissors":
            print("Result: You Win")
            user_score += 1
        else:
            print("Result: You Lose")
            computer_score += 1
    elif user == "paper":
        if computer == "rock":
            print("Result: You Win")
            user_score += 1
        else:
            print("Result: You Lose")
            computer_score += 1
    elif user == "scissors":
        if computer == "paper":
            print("Result: You Win")
            user_score += 1
        else:
            print("Result: You Lose")
            computer_score += 1
    else:
        print("Invalid input")
        continue

    print("Score")
    print("User:", user_score)
    print("Computer:", computer_score)

    again = input("Do you want to play again? (yes/no): ").lower().strip()
    if again != "yes":
        break

print("Game Over")

