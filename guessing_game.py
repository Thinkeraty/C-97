import random

print("---- Number Guessing Game ----")
print("Guess a number between 1 and 9")

number = random.randint(1, 9)
chances = 0

while chances < 5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct!")
        print("You Win!")
        break
    elif guess > number:
        print("Too big! Guess lower than", guess)

    else:
        print("Too small! Guess higher than", guess)

    chances = chances + 1    
    
if not chances < 5:
    print("You lose!")
    print("The Number: ")
    print(number)