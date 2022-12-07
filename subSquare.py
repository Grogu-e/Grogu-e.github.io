# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:58:52 2022

@author: anacs
"""
from random import randint 

  
# SubtractionSquare
def SubtractionSquare():
    
  print("Welcome to SubtractionSquare!")
  player_score = 0
  while True:
    num1 = randint(1,20)
    num2 = randint(1,20)
    answer = num1 - num2
    print(f"What is {num1} - {num2}?")
    player_answer = int(input())
    if player_answer == answer:
      player_score += 1
      print("Correct!")
    else:
      print("Incorrect!")
      break
  print(f"Your score is {player_score}")
