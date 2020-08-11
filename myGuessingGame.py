# Import the random module.
import random

#Create a number_of_guesses variable with a `0` starting point. 
number_of_guesses = 0

#Greet user and prompt for user's name
# Retrun users name and prompt question 'Do you want to play a game?' 
print("Hi Friend!")
name = input('What is your name? ')
print("Do you want to play a game " + name + "?")

#If user says 'y' continue with game, if user says 'n' print 'Okay, sorry for asking then...' 
question = input(str('[y/n] '))
if question == str("y" or "yes" or "yea" or "yeah" or "Y" or "Yes" or "Yea" or "Yeah"):
    print("I have picked a number between 1-15 and I will give you 5 chances to correctly guess the number I am thinking of.")
    
    #Use random.randint method to return a random number from minimum '1' to maximum '15'.
    number = random.randint(1,15)
    
    # While the number os user guesses is below five keep running the loop.
    while number_of_guesses < 5:
        print("What is your guess?")
        guess = input ()
        guess = int(guess)

        #Add one number of use guess everytime the while loop is made.
        #Print string depending if number is higher or lower than the random number chosen.
        number_of_guesses = number_of_guesses + 1
        if guess < number:
            print('That number is too low.')
        if guess > number:
            print('That number is too high.')
        if guess == number:
            break
    
    #When user guesses corret number print string.
    if guess == number:
        number_of_guesses = str(number_of_guesses)
        print('Great Job ' + name + '! , you guessed the number in ' + number_of_guesses + ' attempts.')
    
    #When user guesses incorrect number print string.
    if guess != number:
        number = str(number)
        print('Sorry! ' + name + 'The number I was thinking of was ' + number + '.')    
  
#If user responds 'n' to question run string. 
if question == str("n" or "N" or "no" or "NO" or "nah"):
    print("Okay, sorry for asking then... ")


