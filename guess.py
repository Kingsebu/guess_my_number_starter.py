#importing random package into python
import random

# generating a random secret number which is hidden from user
secret = random.randint(30, 50)

#printing out infomation for the user on the range of the number
print('I am thinking of a whole number between 1 and 99')

#user to enter a guess
guess = int(input("Enter a guess: "))

#setting up counts to count the number times attempts was made
count = 1

'''
using the while loop command to generate the code. As long as the guessed number is not 
equal to the secret number the user will be told whether the number is higher or lower than the secret
number. Where the correct number is guessed the user is congratulated on the guessing right.
'''
while secret != guess:
    if guess < secret:
        count += 1
        print("Your guess is too low. Try again!")
        guess = int(input("Enter a guess: "))
    else:
        count += 1
        print("Your guess is too high, Try again!")
        guess = int(input("Enter a guess: "))

print("Congrats! You guessed right after", count, 'attempts!')
