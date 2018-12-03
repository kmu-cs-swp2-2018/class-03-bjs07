import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count  = 0
        self.maxLen = 0;
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1
            if  self.maxLen < len(word):
                self.maxLen = len(word)

        print('%d words in DB' % self.count)

    def getMaxLength(self):
        return self.maxLen

    def randFromDB(self, minLen = 0):
        if minLen > self.maxLen:
            print("길이 설정 오류! 가장 긴 단어의 길이는 " + str(self.maxLen) + "입니다.")
            print("단어의 길이를 " + str(self.maxLen) + "으로 설정하여 선택합니다.")
            minLen = self.maxLen
        

        while True:
            r = random.randrange(self.count)
            if len(self.words[r]) >= minLen:
                break;

        return self.words[r]
