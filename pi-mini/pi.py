# Pi found using the Mandlebrot Set
def pi(precision=3):
    c = .25 + pow(10, -2*precision)
    x = count = 0
    while x <= 2:
        x = x**2 + c
        count += 1
    return count/(10**precision)