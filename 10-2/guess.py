class Guess:

    def __init__(self, word):
        self.numTries=0 #시도횟수
        self.guessedChars=[] #찾아본 단어
        self.secretWord=word
        self.currentStatus='_'*len(word)

    def display(self): #칸 나타내기
        print(self.currentStatus)
        print("Tries: %d" %self.numTries)
        print(self.secretWord)
        print(self.guessedChars)

    def guess(self, character):

        #주어진 글자를 사용한 글자에 추가
        self.guessedChars.append(character)
        #비밀단어에 주어진 글자가 없으면 틀린 횟수 증가
        if character in self.secretWord:
            for n in range(len(self.secretWord)):
                if character==self.secretWord[n]:
                    self.currentStatus=self.currentStatus[:n]+self.secretWord[n]+self.currentStatus[n+1:]

        # 없으면 틀린 횟수 증가
        else:
            self.numTries +=1

        if self.currentStatus ==self.secretWord:
            return True
        else:
            return False
