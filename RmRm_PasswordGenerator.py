"""
Created on Mon Sep 23 21:43:05 2024

@author: rimae
"""


#Password Generator Project

import random

def pass_gen():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the Rmrm Password Generator!\n")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    
    ## Condition on the input added:
        
        #number of letters
    if nr_letters == 0:
        print("A passowrd with no letters can be easy to predict, try again.\n")
        return pass_gen() 
    
    nr_symbols = int(input("How many symbols would you like?\n"))
    
    ## Condition on the input added:
    
        #number of symbols
    if nr_symbols == 0:
        print("A passowrd with no symbols can be easy to predict, try again.\n")
        return pass_gen()
    
    nr_numbers = int(input("How many numbers would you like?\n"))
       
    ## Condition on the input added:
        
            #number of numbers
    if nr_numbers == 0:
        print("A passowrd with no numbers can be easy to predict, try again.\n")
        return pass_gen()
     
    ## Condition on the input is added:
        #number of total characters:
    if nr_letters + nr_symbols + nr_numbers < 5 :
        print("Your password is less than 5 characters, try again.\n")
        return pass_gen()
    
    ###########################################
    
    # Shuffle the letters list in place
    random.shuffle(letters)

    resultA = []  # To store the results from the loop
    for i in range(nr_letters):  # Repeat nr_letters times
        resultA.append(letters[i]) #add the items "i" from the shuffled list to the new list  "result"
    #to join all the items in the list result we use ''.join(result) | To have spaces between the items ' '.join(words) is used.

    random.shuffle(symbols)
    resultB = [] 
    for i in range(nr_symbols): 
        resultB.append(symbols[i]) 

    random.shuffle(numbers)
    resultC = []

    for i in range(nr_numbers):
        resultC.append(numbers[i])

    final_result = resultA +  resultB + resultC

    random.shuffle(final_result)
    ABC = ''.join(final_result)

    print(f"Your password is: {ABC}\n")
     
    if len(str(ABC)) < 8:
        print("Your password is: Weak.\n")
    elif 8 < len(str(ABC)) < 10:
        print("Your password is: Medium.\n")
    else:
        print("Your password is: Strong.\n")
        
    
while True:
    pass_gen()
    regenerate = input("Do you want to genrate a new password? yes or no.\n".strip().lower())
    if regenerate == "no":
        break
    


     
    
    
