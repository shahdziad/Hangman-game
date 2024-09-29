#Hangman game
#First import the module random

import random
#We started the game by welcoming the player

game= input("Welcome! this is the hangman game, would you like to play? ")
print("That's great! let's get started")
#Make lists of random words for the computer to choose from
 
animals= ["zebra", "ladybug", "dog", "rhinoceros", "alligator", "donkey", "monkey", "lion",
          "cat"]
fruits= ["mango", "apple", "pineapple", "pears", "guava", "banana", "grapes", "cherry",
         "peaches"]
objects= ["table", "drawer", "cubboard", "computer", "pen", "rubber", "window", "necklace",
          "bracelet"]

words= animals+ fruits+ objects
random_word= random.choice(words)
#Define number of chances the player has which will be equal to the length of chosen word

chances= len(random_word)
print("you have", chances,"chances")
player_guess= ""

#Give the player a hint

if random_word in animals:
    print("Hint: it's an animal")
elif random_word in fruits:
    print("Hint: it's a fruit")
else:
    print("Hint: it's an object")

while chances > 0:
    failed_attempts= 0
    for chr in random_word:
        if chr in player_guess:
            print(chr, end=" ")
        else:
            failed_attempts += 1
            print("_", end=" ")
    if failed_attempts== 0:
        print("\nyou won! the word indeed is "+ random_word)
        break
    guesses= input("\nEnter your letter: ")
    player_guess += guesses 
    if guesses not in random_word:
        chances -=1
        print(f"you're wrong, try again. you now have {chances} chances")
        if chances == 0:
           print("Game over. the secret word is", random_word)












   

