# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:05:45 2022

@author: anacs
"""

"""
1. connect to TOPCAT using astropy.io.fits
2. download a sample FITS file
3. print its relevant information
"""

#from astropy.io import fits

# connect to TOPCAT
#hdulist = fits.open('http://www.star.bris.ac.uk/~mbt/topcat/sun.fits')

# print the relevant information
#print(hdulist.info())

# close the connection
#hdulist.close()
from random import randint 

# DivisionDucks
def DivisionDucks():
  print("Welcome to DivisionDucks!")
  player_score = 0
  while True:
    num1 = randint(1,20)
    num2 = randint(1,20)
    answer = num1 // num2
    print(f"What is {num1} // {num2}?")
    player_answer = int(input())
    if player_answer == answer:
      player_score += 1
      print("Correct!")
    else:
      print("Incorrect!")
      break
  print(f"Your score is {player_score}")