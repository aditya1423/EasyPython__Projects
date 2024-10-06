
#get number  9:59:50

import random

random_num= random.randint(1,100)
count=0
max_attempts=5

while True :
    userChoice = input("Guess the Number :")
    if(userChoice=="Quit"):
        print("You want to exit the game .")
        break
    userChoice=int(userChoice)
    count += 1  # Increment count after each guess
    
    if(count > 5):
        break
    if(userChoice==random_num):
        print("you win the game !!! " , random_num)
        break
    elif(userChoice < random_num):
        print("guess bigger no  ")
    else:
        print("Guess smaller no ")    
    
    if count  >= max_attempts:
        print("Sorry !!! You reach the limits ...")
        print("The correct number was" , random_num)
        
 
print(" ------------ GAME OVER ------------")



 

  
    




















