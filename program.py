import math 

def pi_tothe(n):
    if n > 15:
        return 'Error: Too many decimal places, make sure your input is less than 16'

    pistring = str(math.pi)
    newpi = float(pistring[:2+n])
    return newpi

print(pi_tothe(5))


