import random
print("Two player Dice game")

while True:
    input("Player 1-pass Enter to roll")
    p1=random.randint(1,6)
    print("player 1 got:" ,p1)
    
    input("Player 2-pass Enter to roll")
    p2=random.randint(1,6)
    print("player 1 got:" ,p2)
    
    if p1>p2:
        print("Player 1 wins!")
    elif p2>p1:
        print("Player 2 wins!")
    else:
        print("it's a draw!")
        
    again =input("play again ? (y/n):")
    if again!='y':
        break