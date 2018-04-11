import random
import string

WORDLIST_FILENAME = "palavras.txt"

#Carrega palavras
def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    #Abre o arquivo de palavras no modo read;
    #função para abrir arquivo
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    #ler até a próxima linha;
    #ler arquivo-   
    line = inFile.readline()
    # wordlist: list of strings
    #Objeto do tipo string, retorna uma lista de palavras 
    wordlist = str.split(line)
    #Retorna a quantidade de palavras no wordlist
    print ("  ", len(wordlist), "words loaded.")
    #retorna uma palavra randomica
    return random.choice(wordlist)

#
def isWordGuessed(secretWord, lettersGuessed):
    #lista de letras 'secretas'
    secretLetters = []

    for letter in secretWord:
        if letter in secretLetters:
            #Adiciona uma letras no secretLeters
            secretLetters.append(letter)
        else:
            pass

    for letter in secretWord:
        #Se a letra já foi escolhida: passa
        if letter in lettersGuessed:
            pass
        else:
            return False
    
    #se for a certa retorna true
    return True

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def Count_letters_notEqual(secretWord):
    word=[]
    for letter in secretWord:
        if letter not in word:
            word.append(letter)
    print('This Word has', len(word),'different letters')

def hangman(secretWord):
    #chances
    guesses = 8
    lettersGuessed = []
    print ('Welcome to the game, Hangam!')
    print ('I am thinking of a word that is', len(secretWord), ' letters long.')
    Count_letters_notEqual(secretWord)
    print ('-------------')

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print ('You have ', guesses, 'guesses left.')
        #armazena as letras disponiveis
        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print ('Available letters', available)
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Good Guess: ', guessed)
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Oops! That letter is not in my word: ',  guessed)
        print ('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print ('Congratulations, you won!')
        else:
            print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')




secretWord = loadWords().lower()
hangman(secretWord)
