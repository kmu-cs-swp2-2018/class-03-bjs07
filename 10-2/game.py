from hangman import Hangman
from guess import Guess
from word import Word
#알파벳 안에 있는지 검사하기 위한 전역변수
global alphabet
alphabet='abcdefghijklmnopqrstuvwxyz'

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
        
        #lstrip을 넣어서 공백은 자동으로 제거
        guessedChar = input('Select a letter: ')
        if len(guessedChar.lstrip()) != 1:
            print('One character at a time!')
            continue
        if guessedChar.lstrip() in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue
        # 입력한 문자가 알파벳 소문자가 아니면 오류
        if guessedChar.lstrip() not in alphabet:
            print('Character must be English small letter!')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
        print('The answer is '+guess.secretWord)
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
