#number guessing game
import random

secret_number = random.randint(1, 100)
print("welcome to the number guessing game!")

attempts = 0
while True:
    guess=int(input("Enter the guess:"))
    attempts +=1
    
    if guess<secret_number:
        print("To low! try again.")
    elif guess>secret_number:
        print("To high! Try again.")
    else:
        print(f"congratulations! You guessed it in {attemps} attempts.")
        break