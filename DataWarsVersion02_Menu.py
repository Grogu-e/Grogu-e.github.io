# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:00:08 2022

@author: anacs


"""
import DataWars_Logic02 as logic
#import re

#import dataman_logic as logic
#import dataman_data as data
#import random 
import time

from addAlley import AdditionAlley
from subSquare import SubtractionSquare
from MultipliMetro import MultiplicationMetro 
from DiviDucks import DivisionDucks


class DataWars_UI:
    def __init__(self):
        
        self.logic = logic.DataWars_Logic()
        self.data = logic.DataWars_Data()
    
   
    
   
    def displayMenu(self):
        
        
        
        
        #Introduction to DATA WARS
        #
        #Let player beging the quest of Data Wars. 
        print("Welcome To Data Wars")
        print("Step 1: Select your avatar ..")
        print("Step 2: Select difficulty")
        print("Step 3: Let the  Data Wars Begin!!")
        
        
        
       

    def menu(self):
        
        QUIT_CHOICE = 5
        choice = 0
        
        while choice != QUIT_CHOICE: 
            
            self.displayMenu()
            
            choice = int(input("Make A Selection: "))
            if choice == 5: # Exit
                return False # UI is finished
            if choice == 1 :
                self.Avatar()
            elif choice == 2 :
                self.Difficulty()
            elif choice == 3 :
                self.Game()
            else:
                print("Please make another selection.")
                return True 
    
        
       
        # print("Welcome To Data Wars")
        # time.sleep(1)
        # self.Avatar()
        # print(f'Your avatar is {avatar}')
        # time.sleep(1)
        # print("2.Memory Bank ")
        # print("3.Number Guesser ")
        # print("5.Exit")
       
    def Avatar(self):
        #avatar selection
        avatars = ['Knight','Wizard', 'Pirate', 'Robot', 'Ninja']
        print('Please choose an avatar')
        for i in range(len(avatars)):
            print(f'{i+1}. {avatars[i]}')
            
            
        avatar_choice = int(input())
        avatar = avatars[avatar_choice -1]
        print(f'You have choosen {avatar}')    

       
        
        
        
    def Difficulty(self):
         # difficulty selection
         difficulty_levels = ['Easy', 'Medium', 'Hard']
         print('Please choose a difficulty level: ')
         for i in range(len(difficulty_levels)):
             print(f'{i+1}. {difficulty_levels[i]}')
             
             
         difficulty_choice = int(input())
         difficulty = difficulty_levels[difficulty_choice -1]
         print(f'You have chosen {difficulty}')
        
        
        
    def Game(self):
        
        
       
        print("Choose your level:")
        print("1. AdditionAlley")
        print("2. SubtractionSquare")
        print("3. MultiplicationMetro")
        print("4. DivisionDucks")

        level = int(input())
        if level == 1:
          AdditionAlley()
        elif level == 2:
          SubtractionSquare()
        elif level == 3:
          MultiplicationMetro()
        elif level == 4:
          DivisionDucks()
        else:
          print("Invalid level!")
          
    # def displayGame(self):
    #     print("The Game is Starting!")
    #     print("Your Avatar:", self.logic.getAvatar())
    #     print("Difficulty:", self.logic.getDifficulty())
    #     print("Good Luck!")
    
    # def playGame(self):
    #     #self.displayGame()
    #     question_type = self.logic.getQuestion()
        
    #     if question_type == "Addition":
    #         print("Addition Question")
    #         print("")
    #         game = AdditionAlley()
    #         game.play()
            
    #     elif question_type == "Subtraction":
    #         print("Subtraction Question")
    #         print("")
    #         game = SubtractionSquare()
    #         game.play()
            
    #     elif question_type == "Multiplication":
    #         print("Multiplication Question")
    #         print("")
    #         game = MultiplicationMetro()
    #         game.play()
            
    #     elif question_type == "Division":
    #         print("Division Question")
    #         print("")
    #         game = DivisionDucks()
    #         game.play()
        
    # def playAgain(self):
    #     print("Do you want to play again?")
    #     print("1. Yes")
    #     print("2. No")
    #     again = int(input("Make A Selection: "))
    #     if again == 1:
    #         self.Game()
    #     elif again == 2:
    #         self.menu()
    #     else:
    #         print("Invalid Selection")
    #         self.playAgain()      
    
          
          
    
    # def ContinueGame(self,contLoop,checkLoop):
    #     while contLoop == False:
    #         cont = input("Continue Y/N -->")
    #         if cont.lower() == "y":
    #             contLoop = True
    #             print("")
    #         elif cont.lower() == "n":
    #             return False
    #         else:
    #             print("Invalid Input!")
                
                
                
  
        
        
        
        
        
    
    
  
# just set up and launch the UI          
        
def main():
    app = DataWars_UI()
    app.menu()
        
        
if __name__ == "__main__":
    main()
         