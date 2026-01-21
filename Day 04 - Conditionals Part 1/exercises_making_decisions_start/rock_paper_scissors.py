import random

computer_choice = random.randint(0,2)

user_choice = int(input("Scissors (0), Rock (1), Paper (2): "))

if computer_choice == 0:
    computer_choice_name = "scissors"
elif computer_choice == 1:
    computer_choice_name = "rock"
else:
    computer_choice_name = "paper"

if user_choice == 0:
    user_choice_name = "scissors"
elif user_choice == 1:
    user_choice_name = "rock"
else:
    user_choice_name = "paper"

if user_choice > computer_choice:
    print(f"The computer is {computer_choice_name}. You are {user_choice_name}. You win")

elif user_choice < computer_choice:
    print(f"The computer is {computer_choice_name}. You are {user_choice_name}. You lose.")
          
else:
    print(f"The computer is {computer_choice_name}. You are {user_choice_name}. It's a draw.")
    

    
    