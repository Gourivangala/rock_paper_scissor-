import random

# Simple function to get the computer's move
def computer_move():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

# Get the player's move with some basic validation
def player_move():
    move = input("Pick one (rock, paper, or scissors): ").strip().lower()
    while move not in ['rock', 'paper', 'scissors']:
        print("Hmm, that's not a valid choice.")
        move = input("Try again (rock, paper, or scissors): ").strip().lower()
    return move

# Decide who wins
def check_winner(player, computer):
    print(f"\nYou chose {player}, and the computer chose {computer}.")

    if player == computer:
        return "It's a tie!"
    if player == 'rock':
        return "You win!" if computer == 'scissors' else "Computer wins!"
    if player == 'paper':
        return "You win!" if computer == 'rock' else "Computer wins!"
    if player == 'scissors':
        return "You win!" if computer == 'paper' else "Computer wins!"

# Main loop to play the game
def play():
    print("Let's play Rock-Paper-Scissors!")
    while True:
        player = player_move()
        computer = computer_move()
        result = check_winner(player, computer)
        print(result)

        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Alright, thanks for playing!")
            break

# Kick it off
if __name__ == "__main__":
    play()
