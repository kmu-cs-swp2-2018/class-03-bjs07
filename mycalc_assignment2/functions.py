from calcFunctions import *

functionMap=[

    ('factorial(!)',factorial),
    ('-> binary',decToBin),
    ('binary -> dec',binToDec),
    ('-> roman',decToRoman),
    ('roman -> dec', romanToDec),


]

functionList=[x[0] for x in functionMap]