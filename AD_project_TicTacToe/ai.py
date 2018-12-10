import random

class AI:
    def __init__(self, level):
        self.level = level

    def guess(self, current, turn):
        if self.level == "easy":
            return self.getRandomCoordinate(current)

        elif self.level == "normal":
            horizonRepeatNum  = [[0, 0] for i in range(3)]
            verticalRepeatNum = [[0, 0] for i in range(3)]
            diagonalRepeatNum = [[0, 0] for i in range(2)]
            self.getHVDnum(current, horizonRepeatNum, verticalRepeatNum, diagonalRepeatNum)

            # if horizon repeat num is 2  
            row, col = self.getDobuleCoordinate(current, horizonRepeatNum, verticalRepeatNum, diagonalRepeatNum)
            if row != -1:
                return row, col

            # if don't exist repeat num 2
            return self.getRandomCoordinate(current)

        elif self.level == "hard":
            if turn == 1:
                # center opening
                if current[1][1] == 0:
                    return 0, 0
                # edge opening
                elif current[1][0] == 0 or current[0][1] == 0:
                    return 0, 0
                elif current[2][1] == 0 or current[1][2] == 0:
                    return 2, 2
                # corner opening
                else:
                    return 1, 1

            horizonRepeatNum  = [[0, 0] for i in range(3)]
            verticalRepeatNum = [[0, 0] for i in range(3)]
            diagonalRepeatNum = [[0, 0] for i in range(2)]
            self.getHVDnum(current, horizonRepeatNum, verticalRepeatNum, diagonalRepeatNum)

            # if horizon repeat num is 2
            row, col = self.getDobuleCoordinate(current, horizonRepeatNum, verticalRepeatNum, diagonalRepeatNum)
            if row != -1:
                return row, col

            # if exist fork
            for hor in range(3):
                for ver in range(3):
                    if (horizonRepeatNum[hor][0] == 1 and horizonRepeatNum[hor][1] == 0) and (verticalRepeatNum[ver][0] == 1 and verticalRepeatNum[ver][1] == 0) and current[hor][ver] == -1:
                        return hor, ver

            if diagonalRepeatNum[0][0] == 1 and diagonalRepeatNum[0][1] == 0:
                for hor in range(3):
                    if horizonRepeatNum[hor][0] == 1 and horizonRepeatNum[hor][1] == 0 and current[hor][hor] == -1:
                        return hor, hor
                for ver in range(3):
                    if verticalRepeatNum[ver][0] == 1 and verticalRepeatNum[ver][1] == 0 and current[ver][ver] == -1:
                        return ver, ver

            if diagonalRepeatNum[1][0] == 1 and diagonalRepeatNum[1][1] == 0:
                for hor in range(3):
                    if horizonRepeatNum[hor][0] == 1 and horizonRepeatNum[hor][1] == 0 and current[hor][2 - hor] == -1:
                        return hor, 2 - hor
                for ver in range(3):
                    if verticalRepeatNum[ver][0] == 1 and verticalRepeatNum[ver][1] == 0 and current[ver][2 - ver] == -1:
                        return ver, 2 - ver

            # if don't exist repeat num 2
            return self.getRandomCoordinate(current)




    def getRandomCoordinate(self, current):
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            while current[row][col] != -1:
                row = random.randint(0, 2)
                col = random.randint(0, 2)

            return row, col

    def getHVDnum(self, current, horizonRepeatNum, verticalRepeatNum, diagonalRepeatNum):
        # get RepeatNum
        for row in range(3):
            for col in range(3):
                currentValue = current[row][col]
                if currentValue == -1:
                    continue

                horizonRepeatNum[row][currentValue] += 1
                verticalRepeatNum[col][currentValue] += 1

                if row == col:
                    diagonalRepeatNum[0][currentValue] += 1
                if row == 2 - col:
                    diagonalRepeatNum[1][currentValue] += 1

    def getDobuleCoordinate(self, current, horizonRepeatNum, verticalRepeatNum, diagonalRepeatNum):
        for row in range(3):
            if horizonRepeatNum[row][0] == 2 or horizonRepeatNum[row][1] == 2:
                for col in range(3):
                    if current[row][col] == -1:
                        return row, col

        # if vertical repeat num is 2
        for col in range(3):
            if verticalRepeatNum[col][0] == 2 or verticalRepeatNum[col][1] == 2:
                for row in range(3):
                    if current[row][col] == -1:
                        return row, col

        # if digonal repeat num is 2
        if diagonalRepeatNum[0][0] == 2 or diagonalRepeatNum[0][1] == 2:
            for i in range(3):
                if current[i][i] == -1:
                    return i, i

        if diagonalRepeatNum[1][0] == 2 or diagonalRepeatNum[1][1] == 2:
            for i in range(3):
                if current[i][2 - i] == -1:
                    return i, 2 - i

        return -1, -1