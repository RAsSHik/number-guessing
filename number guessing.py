import pyfiglet
import random
import os

def play_again():
    if input("want to play again(y/n)")=="y":
        game()
    else:
        os.system('cls')
def game():
    chosen=random.randint(1,100)
    print(chosen)
    if input("choose level(type e for easy/type h for hard): ")=="easy":
        n=10
    else:
        n=5
    turn=0
    print(f"you have {n} chances")
    while turn<n:
        guess=int(input("guess the number: "))
        if chosen>guess:
            print("too low")
            turn=turn+1
            print(f"you are left with {n-turn} chances")
        elif chosen<guess:
            print("too high")
            turn=turn+1
            print(f"you are left with {n-turn} chances")
        elif chosen==guess:
            print(f"{chosen} is the right answer")
            play_again()
            
    
    if turn==n:
        print(f"game over,right answer was {chosen}.")
        play_again()
print(pyfiglet.figlet_format("hello kk"))
game()

        
