import random
number = random.randrange(1, 10)
guess = int(input("Enter any number: "))
while number != guess:
    if guess < number:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > number:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")
