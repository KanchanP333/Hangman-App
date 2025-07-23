import random
from words import words #importing the array
import string

def getValidWord(words):
    word=random.choice(words) #Will randomly choose a word from the list

    while '-' in word or ' ' in word:
        word=random.choice(words) #Keep iterating until we receive a valid word
    
    return word.upper() 

def hangman():
    word = getValidWord(words)

    wordLetters = set(word) #Unique collection of letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters=set() #To keep track of what the user has guessed

    lives=6
    #Loops until the user has guessed all the letters

    while len(wordLetters)>0 and lives>=1:
        
        print(f"You have {lives} left")
        print("You have used these letters: ",", ".join(usedLetters))
        wordList=[letter if letter in usedLetters else "-" for letter in word]
        #Adds a dash for the letters that have not yet been guessed
        
        print("Current word: "," ".join(wordList))

        userLetter=input("Guess a letter: ").strip().upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives-=1 #Used to take away a life
        
        elif userLetter in usedLetters:
            print("You have already used that character. Please try again!")
        
        else:
            print("Invalid input")
    
    if lives==0:
        print("Sorry you died! The word was", word)
    else:
        print(f"Congrats! You have guessed the word {word}")
    

#main program
hangman()

