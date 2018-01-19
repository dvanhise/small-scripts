import random
import sys

# rolling x dice of special success distribution to get enough successes
def main():
  
    if len(sys.argv) != 3:
        print("Usage: die-calc2 <dice number> <trials>")
        sys.exit(1)
        
    sides = [-1,0,1,1,2,2]
    num = int(sys.argv[1])
    minSum = 1
    maxSum = 8
    trials = int(sys.argv[2])
    
    prob = [0] * (maxSum * max(sides))
    
    for i in range(trials):
        total = 0
        for die in range(num):
            total += random.choice(sides)
        prob[total] += 1
    
    for i in range(minSum, maxSum+1):
        print("{0}: {1:.2f}%".format(i, 100*(1-sum(prob[i:])/trials)))
  
if __name__ == "__main__":
    main()
