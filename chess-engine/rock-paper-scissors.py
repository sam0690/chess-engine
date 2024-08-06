import random

def get_choices():
  player_choice = input("Enter a choice (rock , paper or scissors) : ")
  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice,"computer": computer_choice}

  return choices

def check_win(player,computer):
  print(f"you chose {player},compuer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "scissors cuts paper! You lose."
  elif player == "scissors":
    if computer == "paper":
     return "scissors cuts Paper! You win!"
    else:
      return "Rock smashes paper! You lose."


choices = get_choices()

result = check_win(choices["player"],choices["computer"])
print(result)



