# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:01:17 2022

@author: anacs
"""
from random import randint 




# MultiplicationMetro
def MultiplicationMetro():
  print("Welcome to MultiplicationMetro!")
  player_score = 0
  while True:
    num1 = randint(1,20)
    num2 = randint(1,20)
    answer = num1 * num2
    print(f"What is {num1} * {num2}?")
    player_answer = int(input())
    if player_answer == answer:
      player_score += 1
      print("Correct!")
    else:
      print("Incorrect!")
      break
  print(f"Your score is {player_score}")