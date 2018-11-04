from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    romans = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
              ]
    try:
        n=int(numStr)
        result=''
        for value,letters in romans:
            while n>=value:
                result+=letters
                n-=value
        return result



    except:
        return 'dec -> Roman'

def romanToDec(numStr):
    romans = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
              ]
    try:

        ret=0
        while len(numStr)!=0:
            for x in romans:
                while numStr[0:len(x[1])]==x[1]:
                    numStr=numStr[len(x[1]):]
                    ret+=x[0]
        return ret
    except:
        return 'Error!'
