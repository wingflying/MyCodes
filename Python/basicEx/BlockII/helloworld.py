import random

secret = random.randint(1, 99)
guess = int(0)
tries = int(0)

print("HOXTON I am the Dread pirate roberts,and i have a secret!\n")
print("It is a number from 1 to 99. I will give you 6 tries.\n")

while guess != secret and tries < 6:
    guess_input = input("what is  your guess?")
    try:
        guess = int(guess_input)
        if guess < secret:
            print("too low, ye scurvy dog!")
        elif guess > secret:
            print("too high, landlubber!")
        tries = tries + 1
    except ValueError:
        print("That's not a valid number! Try again.")

if guess == secret:
    print("avast!ye got it!found my secret,ye did!")
else:
    print("no more guesses! better luck next time,matey!")
    print("the secret number was", secret)
