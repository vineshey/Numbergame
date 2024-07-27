import random
number=random.randint(1,100)
guess=0
count=0
while guess!=number:
    guess=int(input("Enter Your Guess(1-100):"))
    count= count+1
    if guess<number:
        print("Guess Higher")
    elif guess>number:
        print("Guess Lower")
    else:
        print(f"you won in {count} Attempts")
