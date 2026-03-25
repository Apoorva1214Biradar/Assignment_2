#Create a number guessing game where the computer picks a random number between 1-100 and the user gets 7 attempts. 
# Rules: 
# 1. After each guess, show if guess is too high or too low and attempts remaining 
# 2. If correct: congratulate and show attempts used 
# 3. If failed: reveal the number 
# 4. Ask to play again

import random  # Import random module 

best_score = None  # best (minimum) as  none 

while True:  #  outer  loop is applied so the game can repeat (i.e play again)
    num = random.randint(1, 100)  # random number between 1 and 100 
    attempts_left = 7             # it defines Player has 7 attempts
    attempts_used = 0             # Count how many guesses the player used initially defined to zero

    print("\nGuess the number (1–100). You have 7 attempts.") 
    while attempts_left > 0:  # Loop while player still has attempts
        guess = int(input("Enter guess: "))  # guess as an input 
        attempts_left -= 1                  # Decrease attempts remaining
        attempts_used += 1                  # Increase attempts used count

        if guess == num:  # If guess equals the secret number
            print(f" Congratulations!!.. You guessed in {attempts_used} attempts.")  # print Success message for user 

            # Check if this is the best score so far or not using if else condition 
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used  # Update the best score
                print("New best score!") 

            break  # Exit
        elif guess < num:  # If guess is smaller than number
            if abs(num - guess) <= 5:  # If guess is within 5 of number
                print(f" Too low ( you are very close!). Attempts left: {attempts_left}")
            else:
                print(f" Too low. Attempts left: {attempts_left}")

        else:  # If guess is greater than number
            if abs(num - guess) <= 5:  # If guess is within 5
                print(f" Too high (you are very close!). Attempts left: {attempts_left}")
            else:
                print(f"Too high. Attempts left: {attempts_left}")

    else:  
        print(f" Out of attempts! The number was {num}")  # Reveal number

    if best_score is not None:  # If at least one game was won
        print("Best score:", best_score, "attempts")  # Show best score

    again = input("Play again? (yes/no): ").lower()  # if they want to play again
    if again != "yes":  # If user does not type yes
        print("Thanks for playing!") 
        break  # Stop outer loop to end game
    
#output 1:

# Guess the number (1–100). You have 7 attempts.
# Enter guess: 55
# Too high. Attempts left: 6
# Enter guess: 40
# Too high. Attempts left: 5
# Enter guess: 30
#  Too high (you are very close!). Attempts left: 4
# Enter guess: 26
#  Too high (you are very close!). Attempts left: 3
# Enter guess: 24
#  Too low ( you are very close!). Attempts left: 2
# Enter guess: 22
#  Too low ( you are very close!). Attempts left: 1
# Enter guess: 25
#  Congratulations!!.. You guessed in 7 attempts.
# New best score!
# Best score: 7 attempts
# Play again? (yes/no): yes



#0utput 2:
# Guess the number (1–100). You have 7 attempts.
# Enter guess: 34
# Too high. Attempts left: 6
# Enter guess: 24
# Too high. Attempts left: 5
# Enter guess: 14
#  Too low ( you are very close!). Attempts left: 4
# Enter guess: 19
#  Too high (you are very close!). Attempts left: 3
# Enter guess: 15
#  Congratulations!!.. You guessed in 5 attempts.
# New best score!
# Best score: 5 attempts
# Play again? (yes/no): yes


