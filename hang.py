import random
import string

WORDLIST_FILENAME = "palavras.txt"


def add_letter(lettersGuessed, letter, a):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print (a,  guessed)

def available_letter(lettersGuessed):
    available = getAvailableLetters()
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
    print ('Available letters', available)

def Count_letters_notEqual(secretWord):
    word=[]

    for letter in secretWord:
        if letter not in word:
            word.append(letter)
    print('This Word has', len(word),'different letters')

def game_result(lettersGuessed):
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print ('Congratulations, you won!')
    else:
        print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')


def getAvailableLetters():
    import string
    available = string.ascii_lowercase

    return available

def getGuessedWord():
     guessed = ''

     return guessed

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    message_begin()
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print ('You have ', guesses, 'guesses left.')
        a = "Good Guess: "
        b = "Oops! That letter is not in my word: "
        c = "'Oops! You have already guessed that letter: "

        available_letter(lettersGuessed)
        letter = input('Please guess a letter: ')
        if isInt(letter) == True:
            print('Por favor digite uma letra.')
        else:
            if letter in lettersGuessed:
                add_letter(lettersGuessed, letter, c)
                
            elif letter in secretWord:
                lettersGuessed.append(letter)
                add_letter(lettersGuessed, letter, a)

            else:
                guesses -=1
                lettersGuessed.append(letter)
                add_letter(lettersGuessed, letter, b)
    
        print ('------------')
    else:
        game_result(lettersGuessed)
        
        

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in secretLetters:
            secretLetters.append(letter)
        else:
            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    
    return True

def loadWords():

    message_load()
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return random.choice(wordlist)

def message_begin():
    print ('Welcome to the game, Hangam!')
    print ('I am thinking of a word that is', len(secretWord), ' letters long.')
    Count_letters_notEqual(secretWord)
    print ('-------------')

def message_load():
     print ("Loading word list from file...")

def isInt(value):
    try:
        int(value) and float(value)
        return True
    except:
        return False

secretWord = loadWords().lower()
hangman(secretWord)


