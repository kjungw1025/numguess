from random import randint
answer = randint(1, 100)

name = input("what is your name? ")
print("HI, {}".format(name))
guess = int(input("what is your guess number? "))
print("your guess: {}, answer: {}".format(guess, answer))
