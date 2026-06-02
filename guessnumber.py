import random
num=random.randint(1,10)

attemps=3
while attemps>0:
    guess=int(input("Guess the number:"))
    if guess==num:
        print("Correct!")
        break
    elif guess>num:
        print("Too high")
    else:
        print("Too low")
    attemps-=1

if attemps==0:
    print("Game over.Number was:",num)