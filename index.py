import random
import pyfiglet

# Create ASCII art from text
ascii_art = pyfiglet.figlet_format("Rock Paper Scissors")

# Print the ASCII art
print(ascii_art)

while True:
    options = [
    "rock",
    "paper",
    "sccisors"
]
    print()
    player = None
    computer = random.choice(options)
    player = input("your choice (rock paper sccisors): ")
    if player == computer:
       print("tie")
       print(f'computer: {computer}')
    elif player == "rock" and computer == "sccisors":
      print("You win!!")   
      print(f'computer: {computer}')
    elif player == "paper" and computer == "rock":
      print("You Win!!")
      print(f'computer: {computer}')
    elif player == "sccisors" and computer == "paper":
       print("You win!!")
       print(f'computer: {computer}')
    else:
      print("You lose")
      print(f'computer: {computer}')
    if input("play again? (y, n): ") == "y":
       continue
    else:
       break
       
