import random
import sys


def main():
  
    if len(sys.argv) != 5:
        print("Usage: die-calc <die sides> <success> <num of successes> <trials>")
        sys.exit(1)

    sides = int(sys.argv[1])
    minNum = int(sys.argv[2])
    minSuccess = int(sys.argv[3])
    trials = int(sys.argv[4])
    
    for numDice in range(1,11):
        successes = 0
        for i in range(trials):
            numPass = 0
            for j in range(numDice):
                roll = random.randint(1, sides)
                if roll >= minNum:
                    numPass += 1
                    
            if numPass >= minSuccess:
                successes += 1
        print("%d dice: %.1f%%   (%d/%d) success" % (numDice, (successes/trials)*100.0, successes, trials))
  
if __name__ == "__main__":
    main()
