from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    #랜덤으로 단어 선택
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    #목숨의 갯수를 초기화
    maxTries = hangman.getLife()

    while guess.numTries < maxTries: #max

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
