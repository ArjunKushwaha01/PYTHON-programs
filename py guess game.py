import random

# Generate a random number between 1 and 20
random_number = random.randint(1,20)

# Set the number of tries
max_tries = 5
tries = 0

print("Welcome to the Guess the Number game!")
print(f"You have {max_tries} tries to guess the number between 1 and 20.")

while tries < max_tries:
    guess = int(input("Enter your guess: "))
    tries += 1
    
    if guess == random_number:
        print(f"Congratulations! You've guessed the number {random_number} in {tries} tries.")
        break
    elif guess < random_number:
        print("Try higher.")
    else:
        print("Try lower.")

if tries == max_tries and guess != random_number:
    print(f"Sorry, you've run out of tries. The correct number was",{random_number})


































