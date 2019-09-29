import math
def factors(n):
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            print(str(i)+'*'+str(int(n/i)))
            

k=int(input('input integer:\n'))

factors(k)