import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return 'user'
    else:
        return 'computer'

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        return 0, 0  # No score change

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == 'tie':
        print("It's a tie!")
        return 0, 0
    elif winner == 'user':
        print("You win this round!")
        return 1, 0
    else:
        print("Computer wins this round!")
        return 0, 1

def main():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        u, c = play_round()
        user_score += u
        computer_score += c
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
