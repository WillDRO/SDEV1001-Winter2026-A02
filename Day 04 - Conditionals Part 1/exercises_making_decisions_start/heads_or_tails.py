import random

coin_flip = random.randint(0,1)


user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ")

if coin_flip == 0:
    print("The coin landed on heads.")
    
else:
    print("The coin landed on tails.")

# Check if the user's guess is correct or wrong with just one line of if statements
if (user_guess == "h" and coin_flip == 0) or (user_guess == "t" and coin_flip == 1):
    print("You guessed correctly!")
    
else:
    print("You guessed wrong!")
