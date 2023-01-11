from random import randint
from time import sleep
answer = randint(1, 100)

def numguess():
  name = input("what is your name? ")
  print("HI, {}".format(name))
  chance = 5
  while (chance > 0):
      guess = int(input("what is your guess number? (1 ~ 100) "))
      if (guess == answer):
          for _ in range(3):
              sleep(1)
              print("*************")
          print("Correct {}! The answer was {}".format(name, str(answer)))
          return
      elif guess > answer:
          chance -= 1
          print(f"Keep going, man~! That was too high. {name}..")
      elif guess < answer:
          chance -= 1
          print(f"Keep going, man~! That was too low. {name}..")

numguess()

