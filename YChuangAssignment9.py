#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[3]:


#create a function to flip a coin
#use dictionary to map heads and tails to 1 and 0
#flip the coin
def flip_coin():
    flip_dict = {1: "heads",
                0: "tails"}
    coin_toss = flip_dict[random.randint(0,1)]
    
    return coin_toss


# In[4]:


#the function to guess the result of 1 coin flip
def guess_coin_flip():
    #ask user's guess
    user_guess = input("heads or tails?")
    
    #flip the coin
    coin_flip = flip_coin()
    
    #if the guess is correct
    if user_guess == coin_flip:
        print(f"correct! you guessed {user_guess} and the coin landed on {coin_flip}")
        correct_guess = True
    #if the guess is wrong
    elif user_guess != coin_flip:
        print(f"incorrect... you guessed {user_guess} and the coin landed on {coin_flip}")
        correct_guess = False
    #return True or False based on the result    
    return correct_guess


# In[5]:


# function to guess 2 consecutive correct coin flips
def guess_two_coin_flips():
    # set up counters for how many total guesses and how many consecutive successful guesses
    guess_number = 0
    successful_guesses = 0
    # while successful guesses is 0 or 1, guess and flip the coin
    while successful_guesses < 2:
        result = guess_coin_flip()
        
        #if the guess matches the coin flip
        if result == True:
            guess_number += 1
            successful_guesses += 1
        #if the guess doesn't match the coin flip
        elif result == False:
            guess_number += 1
            successful_guesses = 0
            
    print(f"2 successful guesses in a row! It took you {guess_number} guesses")


# In[7]:


guess_two_coin_flips()


# In[ ]:





# In[ ]:




