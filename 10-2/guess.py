class Guess:

    def __init__(self, word):
        self.numTries=0 #시도횟수
        self.guessedChars=[] #찾아본 단어
        self.answer = word #정답 단어
        self.secretWord='_'*len(word)
        self.currentStatus=''
        self.temp=word

    def display(self): #칸 나타내기
        print(self.secretWord)
        print("Tries: %d" %self.numTries)
        print(self.answer)
        print(self.guessedChars)

    def guess(self, character):

        #주어진 글자를 사용한 글자에 추가
        self.guessedChars.append(character)
        self.currentStatus+=character
        #비밀단어에 주어진 글자가 없으면 틀린 횟수 증가
        '''if character in self.answer:
            for i in range(0,len(self.answer)):
                if character == self.answer[i]:
                    self.secretWord[i]=character
        '''

        if character in self.answer:

            n=self.answer.index(character) #단어 인덱스
            self.secretWord=self.secretWord[:n]+self.answer[n]+self.secretWord[n+1:]
            self.numTries-=1
        # 없으면 틀린 횟수 증가
        self.numTries +=1

        if self.secretWord ==self.answer:
            return True
        else:
            return False
