
import random

print ("Guessing Game")
print ("You have 5 chances to guess the number")
print("Guess from  1 to 10")

number_to_guess = random.randrange(1 , 10) # from where to you can generate random number
chances = 5
guess_counter = 0

while guess_counter < chances: #user first attempt and guess counte is less than  user chances
    guess_counter += 1
    my_guess = int(input("Enter Your guess"))
    
    if my_guess == number_to_guess:
        print(f" You guess the number {number_to_guess} and You found it right! in the {guess_counter} attempt")
        break
    elif guess_counter>= chances and my_guess != number_to_guess:
        print(f"Oops! the number is {number_to_guess} better luck next time")
    elif my_guess < number_to_guess:
        print("Your guess is very low, Try Again!")
    elif my_guess > number_to_guess:
        print("Your guess is too high, Try Again!")

