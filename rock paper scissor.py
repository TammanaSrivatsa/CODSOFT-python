import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        player_choice = input("Enter your choice (1/2/3/4): ")

        if player_choice == '4':
            print("Thanks for playing. Goodbye!")
            break
        elif player_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        player_choice = int(player_choice)
        computer_choice = random.randint(1, 3)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 1 and computer_choice == 3) or \
             (player_choice == 2 and computer_choice == 1) or \
             (player_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    play_game()
