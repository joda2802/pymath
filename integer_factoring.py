import math
def factors(n):
    a=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            a.append(i)
            a.append(int(n/i))
    a.sort()
    return a

k=int(input('input integer:\n'))

print(factors(k))