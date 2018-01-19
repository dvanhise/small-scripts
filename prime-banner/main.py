import re
from sympy.ntheory.generate import nextprime


PROTOTYPE_FILE = './example.txt'
OUTPUT_FILE = './output.txt'

def getNumFromFile(filename):
    with open(filename, 'r') as numfile:
        length = len(re.sub(r'[^0-9]', '', numfile.readline()))
        numfile.seek(0)
        numString = re.sub(r'[^0-9]', '', numfile.read())
    return length, int(numString)


def printNumToFile(filename, num, lineLength):
    output = str(num)
    with open(filename, 'w') as outfile:
        for line in range(len(output) // lineLength):
            outfile.write(output[line*lineLength:(line+1)*lineLength] + '\n')

lineLength, baseNum = getNumFromFile(PROTOTYPE_FILE)
prime = nextprime(baseNum)
printNumToFile(OUTPUT_FILE, prime, lineLength)
