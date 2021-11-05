import random

number = random.randint(1, 10)

guess=int(input("Please enter a number:"))

while guess!=number:
 if guess>number:
    print("Decrease your number.")
    guess = int(input("Please enter a number:"))
 else:
    print("Increase your number.")
    guess = int(input("Please enter a number:"))
if guess==number:
    print("Congratulations! Your guess is correct")