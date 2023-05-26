#!/usr/bin/env python
#allynasriaa
import random

def main():
  """Start a song guessing game."""
  print("Guess the song name")

  x = random.choice
  EXO = [
    "love shot",
    "growl",
    "monster",
    "lotto",
    "love me right",
    "call me baby",
    ] 

  x = random.choice(EXO)
  
  guess = None

  while x != guess:

   guess = str(input("what song am i thinking of? "))

   if x == guess:
      print("You guessed {}. Congratulations you got it right!".format(guess))
      break
   else:
      print("you guessed {}. Unfortunately you got the wrong answer. please         try again!".format(guess))

main()