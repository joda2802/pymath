import math
import sys

sys.setrecursionlimit(10000)

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def phi(x):
    if x==1:
        return 0
    if is_prime(x):
        return phi(x-1)+1
    else:
        return phi(x-1)

k=int(input('input integer:\n'))
print(phi(k))