# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:57:42 2022

@author: anacs
"""
# import pygame
# # Intialize the pygame
# pygame.init()

# #create the screen
# screen = pygame.display.set_mode((800,600))

# #Title and Icon
# pygame.display.set_caption("Call of Number War")
# icon = pygame.image.load('city-on-fire.png')
# pygame.display.set_icon(icon)




# #Game loop
# running = True 
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.quit():
#          running = False
         
         
         
#     #RGB - Red, Green, Blue 3
#     screen.fill ((255,0, 0))
#     pygame.display.update()
    
    
from random import randint 

# AdditionAlley
def AdditionAlley():
  print("Welcome to AdditionAlley!")
  player_score = 0
  while True:
    num1 = randint(1,20)
    num2 = randint(1,20)
    answer = num1 + num2
    print(f"What is {num1} + {num2}?")
    player_answer = int(input())
    if player_answer == answer:
      player_score += 1
      print("Correct!")
    else:
      print("Incorrect!")
      break
  print(f"Your score is {player_score}")
           