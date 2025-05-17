import random
import sys

    # get random choice for computer
def computer_choice():
    choices = ('r', 'p', 's')
    computer_chooses = random.choice(choices)

    if computer_chooses == 'r':
        print("Computer chooses 🪨")
    if computer_chooses == 'p':
        print("Computer chooses 📜")
    if computer_chooses == 's':
        print("Computer chooses ✂️")
    return computer_chooses    

   # determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
            (user_choice == 'p' and computer_choice == 'r') or \
            (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"  

def main():
    # welcome message
    print("Welcome to Coomber's Rock, Paper, Scissors game!")
    
    # infinite loop for the game, which will only break when the user chooses to quit
    while True:
        # get user input
        user_input = input("Enter your choice (r, p, s) or 'q' to quit: ").lower()
        if user_input not in ['r', 'p', 's', 'q']:
            print("Invalid choice, please try again.")
            continue
        elif user_input == 'r':
            print("You chose 🪨")
        elif user_input == 'p':
            print("You chose 📜")
        elif user_input == 's':
            print("You chose ✂️")
        elif user_input == 'q':
            print("Play again next time!")
            break
        
        winner = determine_winner(user_input, computer_choice())
        print(winner)
        play_again()

def play_again():
    # ask user if they want to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            return
        elif play_again == 'n':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        

if __name__ == "__main__":
    main()