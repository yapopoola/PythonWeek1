import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 10

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. You have 10 attempts.")

while attempts > 0:
    # Prompt user for a guess
    try:
        guess = int(input(f"Enter your guess (Attempts remaining: {attempts}): "))
        
        # Validate input
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        attempts -= 1
        
        # Check if guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number}!")
            break
        elif attempts == 0:
            print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")


#         # ------------------------


import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)

# Set the maximum number of attempts
max_attempts = 10
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    try:
        # Get user input
        guess = int(input("Enter your guess: "))
        
        # Increment the attempt counter
        attempts += 1
        
        # Check the guess
        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number!")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

if attempts == max_attempts:
    print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")


# #     # -------------------------------

    import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Welcome to the Guessing Game!")

# Loop until the user guesses the correct number or reaches the maximum attempts
while attempts < max_attempts:
    input_number = int(input('Type in your lucky number: '))
    attempts += 1

    if input_number == secret_number:
        print('Congratulations! Correct guess!!!')
        break
    else:
        print('Incorrect guess.')

if attempts == max_attempts:
    print(f'Sorry, you have used all your attempts. The secret number was {secret_number}.')

usernames_and_passwords = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
    "user4": "pass4",
    "user5": "pass5",
    "user6": "pass6",
    "user7": "pass7",
    "user8": "pass8",
    "user9": "pass9",
    "user10": "pass10"
}

attempts = 0

username = input('Username: ')

if username not in usernames_and_passwords:
    print('Invalid User')
else:
    password = input('Password: ')
    
    while usernames_and_passwords[username] != password and attempts < 5:
        print('provide the correct password')
        password = input('Password: ')
        attempts += 1
        
        if attempts >= 5:
            print('Your account has been suspended for 24 hours...')
            break
    
    if usernames_and_passwords[username] == password:
        print('login was successful')