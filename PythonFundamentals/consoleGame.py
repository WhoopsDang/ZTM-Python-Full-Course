import sys
import random

if sys.argv[1] is not None:
    ans = random.choice(range(int(sys.argv[2])))
    guess = int(input(f"Guess a number between {sys.argv[1]} and {sys.argv[2]}"))
else:
    ans = random.choice(range(10))
    guess = int(input(f"Guess a number between {1} and {10} \n"))


while True:
    if guess != ans:
        guess = int(input("oop sorry, u suck. Try again \n"))
    else:
        print(f"Great job! the number was indeed {ans}")
        break
