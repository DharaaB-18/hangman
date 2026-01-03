import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

words = "time year people thing woman life child world school state family student group country problem hand part place case week company system program question work government number night point home water room mother area money story fact month right study book word business issue side kind head house service friend father power hour game line member city community name president team minute idea information parent face level office door health person history party result change morning reason research girl moment teacher force education".split()

def getRandomWord(wordList):
  wordIndex = random.randint(0, len(wordList)-1)
  return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters,secretWord):
  print(HANGMAN_PICS[len(missedLetters)])
  print()

  print("Missed Letters:", end=" ")
  for letter in missedLetters:
    print(letter, end=" ")
  print("\n")

  blanks = "_"*len(secretWord)

  for i in range(len(secretWord)):
    if secretWord[i] in correctLetters:
      blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

  for letter in blanks:
    print(letter, end=" ")



  print()

def getGuess(alreadyGuessed):
  while True:
    guess = input("\nGuess a letter:")
    guess = guess.lower()
    if len(guess) !=1:
      print("Please enter a single letter.")
    elif guess in alreadyGuessed:
      print ("You have already guessed that letter. Choose again.")
    elif guess not in "abcdefghijklmnopqrstuvwxyz": # find better way to do this
      print("Please enter a LETTER.")
    else:
      return guess

def playAgain():
  print("\nDo you want to play again? (yes or no)")
  return input().lower().startswith("y")

print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
  displayBoard(missedLetters, correctLetters, secretWord)

  guess = getGuess(missedLetters + correctLetters)

  if guess in secretWord:
    correctLetters = correctLetters + guess

    foundAllLetters = True
    for i in range(len(secretWord)):
      if secretWord[i] not in correctLetters:
        foundAllLetters = False
        break
    if foundAllLetters:
      displayBoard(missedLetters, correctLetters, secretWord)
      print("\nYes! The secret word is '" + secretWord + "'! You have won!")
      gameIsDone = True
  else:
    missedLetters = missedLetters + guess

    if len(missedLetters) == len(HANGMAN_PICS) - 1:
      displayBoard(missedLetters, correctLetters, secretWord)
      print("\nYou have run out of guesses!\n\nAfter " +
        str(len(missedLetters)) + " missed guesses and " +
        str(len(correctLetters)) + " correct guesses, the word was:\n '" + secretWord + "'")
      gameIsDone = True

  if gameIsDone:
    if playAgain():
      missedLetters = ""
      correctLetters = ""
      gameIsDone = False
      secretWord = getRandomWord(words)
    else:
      break
