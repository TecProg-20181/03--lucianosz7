import random
import string
from functions import loadWords
from functions import hangman


WORDLIST_FILENAME = "palavras.txt"

secretWord = loadWords().lower()
hangman(secretWord)


